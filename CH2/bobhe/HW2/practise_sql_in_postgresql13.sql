CREATE TABLE public.daily_prices (
    symbol text NOT NULL,
    date timestamp without time zone NOT NULL,
    volume double precision,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    dividend double precision,
    ratio_adj double precision,
    volume_adj double precision,
    open_adj double precision,
    close_adj double precision,
    high_adj double precision,
    low_adj double precision,
    dollar_volume double precision,
    updated timestamp without time zone
);


ALTER TABLE ONLY public.daily_prices
    ADD CONSTRAINT daily_prices_pkey PRIMARY KEY (symbol, date);

CREATE UNIQUE INDEX daily_prices_idx ON public.daily_prices USING btree (symbol, date);

-- using index

select symbol , count(*) from daily_prices group by symbol order by symbol;
-- using group by
select symbol, sum(volume) as total_volume from daily_prices group by symbol order by total_volume ;

--get the daily price change percentage by using LEFT JOIN
select curr.date, curr.close_adj, curr.close_adj/pre.close_adj rate
from(
	select date, close_adj, row_number() over (ORDER BY date) as row1
	from daily_prices
	where symbol = 'TSLA'
	ORDER BY date asc) curr
LEFT JOIN(
	select date, close_adj, row_number() over (ORDER BY date) as row2
	from daily_prices
	where symbol = 'TSLA'
	ORDER BY date asc) pre
ON curr.row1=pre.row2+1;


-- Automatically create a partition through using
-- trigger function
-- when there are new records inserting into the master table
-- 创建主表结构, 表名称 tbl_partition, 其中的时间字段名: gather_time
CREATE TABLE tbl_partition
(
  id integer,
  name text,
  data numeric,
  gather_time timestamp
);

CREATE OR REPLACE FUNCTION auto_insert_into_tbl_partition()
  RETURNS trigger AS
$BODY$
DECLARE
    time_column_name 	text ;			-- 父表中用于分区的时间字段的名称[必须首先初始化!!]
    curMM 		varchar(6);		-- 'YYYYMM'字串,用做分区子表的后缀
    isExist 		boolean;		-- 分区子表,是否已存在
    startTime 		text;
    endTime		text;
    strSQL  		text;

BEGIN
    -- 调用前,必须首先初始化(时间字段名):time_column_name [直接从调用参数中获取!!]
    time_column_name := TG_ARGV[0];

    -- 判断对应分区表 是否已经存在?
    EXECUTE 'SELECT $1.'||time_column_name INTO strSQL USING NEW;
    curMM := to_char( strSQL::timestamp , 'YYYYMM' );
    select count(*) INTO isExist from pg_class where relname = (TG_RELNAME||'_'||curMM);

    -- 若不存在, 则插入前需 先创建子分区
    IF ( isExist = false ) THEN
        -- 创建子分区表
        startTime := curMM||'01 00:00:00.000';
        endTime := to_char( startTime::timestamp + interval '1 month', 'YYYY-MM-DD HH24:MI:SS.MS');
        strSQL := 'CREATE TABLE IF NOT EXISTS '||TG_RELNAME||'_'||curMM||
                  ' ( CHECK('||time_column_name||'>='''|| startTime ||''' AND '
                             ||time_column_name||'< '''|| endTime ||''' )
                          ) INHERITS ('||TG_RELNAME||') ;'  ;
        EXECUTE strSQL;

        -- 创建索引
        strSQL := 'CREATE INDEX '||TG_RELNAME||'_'||curMM||'_INDEX_'||time_column_name||' ON '
                  ||TG_RELNAME||'_'||curMM||' ('||time_column_name||');' ;
        EXECUTE strSQL;

    END IF;

    -- 插入数据到子分区!
    strSQL := 'INSERT INTO '||TG_RELNAME||'_'||curMM||' SELECT $1.*' ;
    EXECUTE strSQL USING NEW;
    RETURN NULL;
END
$BODY$
  LANGUAGE plpgsql;

-- 为主表创建触发器, 其中,调用了触发器函数 auto_insert_into_tbl_partition(‘gather_time’)
CREATE TRIGGER insert_tbl_partition_trigger
  BEFORE INSERT
  ON tbl_partition
  FOR EACH ROW
  EXECUTE PROCEDURE auto_insert_into_tbl_partition('gather_time');


INSERT INTO tbl_partition VALUES
(1,'abc',123, '2020-12-23 12:23:26.004');
INSERT INTO tbl_partition VALUES
(1,'abc',123, '2020-11-01 11:23:26.004');
INSERT INTO tbl_partition VALUES
(1,'abc',123, '2020-10-01 10:23:26.004');

SELECT * FROM tbl_partition;
SELECT * FROM tbl_partition_202010;
SELECT * FROM tbl_partition_202011;
SELECT * FROM tbl_partition_202012;