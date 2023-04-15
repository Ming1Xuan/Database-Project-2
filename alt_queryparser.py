import re

def parse_sql_file(file_path):
    # Open the file and read its contents
    #with open(file_path, 'r') as file:
    #    sql_query = file.read()

    #sql_query = "select returnflag, linestatus, sum(linequantity) as sumqty, count(*) as count_order from table where blah1 AND blah4 AND blah5 group by blah 2 order by blah 3"

    # 1.sql-------------------------------------------------------------------------------------------------------------------------------------
    # sql_query = "select\
    #     l_returnflag,\
    #     l_linestatus,\
    #     sum(l_quantity) as sum_qty,\
    #     sum(l_extendedprice) as sum_base_price,\
    #     sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,\
    #     sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,\
    #     avg(l_quantity) as avg_qty,\
    #     avg(l_extendedprice) as avg_price,\
    #     avg(l_discount) as avg_disc,\
    #     count(*) as count_order\
    # from\
    #     lineitem\
    # where\
    #     l_shipdate <= date '1998-12-01' - interval ':1' day\
    # group by\
    #     l_returnflag,\
    #     l_linestatus\
    # order by\
    #     l_returnflag,\
    #     l_linestatus;\
    # "


    # 10.sql-------------------------------------------------------------------------------------------------------------------------------------
    # sql_query = "select\
    #     c_custkey,\
    #     c_name,\
    #     sum(l_extendedprice * (1 - l_discount)) as revenue,\
    #     c_acctbal,\
    #     n_name,\
    #     c_address,\
    #     c_phone,\
    #     c_comment\
    # from\
    #     customer,\
    #     orders,\
    #     lineitem,\
    #     nation\
    # where\
    #     c_custkey = o_custkey\
    #     and l_orderkey = o_orderkey\
    #     and o_orderdate >= date ':1'\
    #     and o_orderdate < date ':1' + interval '3' month\
    #     and l_returnflag = 'R'\
    #     and c_nationkey = n_nationkey\
    # group by\
    #     c_custkey,\
    #     c_name,\
    #     c_acctbal,\
    #     c_phone,\
    #     n_name,\
    #     c_address,\
    #     c_comment\
    # order by\
    #     revenue desc;\
    # "


    # fake20.sql-------------------------------------------------------------------------------------------------------------------------------------
    sql_query = "select\
        s_name,\
        s_address\
    from\
        supplier,\
        nation\
    where\
        s_suppkey in (\
            select\
                ps_suppkey\
            from\
                partsupp\
            where\
                blah1 = blah2 \
        )\
        and s_nationkey = n_nationkey\
        and n_name = ':3'\
    group by\
        s_name\
    order by\
        lastoneee;\
    "


    # 20.sql-------------------------------------------------------------------------------------------------------------------------------------
    # sql_query = "select\
    #     s_name,\
    #     s_address\
    # from\
    #     supplier,\
    #     nation\
    # where\
    #     s_suppkey in (\
    #         select\
    #             ps_suppkey\
    #         from\
    #             partsupp\
    #         where\
    #             ps_partkey in (\
    #                 select\
    #                     p_partkey\
    #                 from\
    #                     part\
    #                 where\
    #                     p_name like ':1%'\
    #             )\
    #             and ps_availqty > (\
    #                 select\
    #                     0.5 * sum(l_quantity)\
    #                 from\
    #                     lineitem\
    #                 where\
    #                     l_partkey = ps_partkey\
    #                     and l_suppkey = ps_suppkey\
    #                     and l_shipdate >= date ':2'\
    #                     and l_shipdate < date ':2' + interval '1' year\
    #             )\
    #     )\
    #     and s_nationkey = n_nationkey\
    #     and n_name = ':3'\
    # order by\
    #     s_name;\
    # "




    # Define regular expressions to match each clause
    select_pattern = re.compile(r'select (.+?) from', re.DOTALL)
    from_pattern = re.compile(r'from (.+?) where', re.DOTALL)
    where_pattern = re.compile(r'where (.+?) (?: group by|order by|$)', re.DOTALL)
    group_by_pattern = re.compile(r'group by (.+?) (?: order by|$)', re.DOTALL)
    order_by_pattern = re.compile(r'order by (.+?)$', re.DOTALL)

    # print("1st CHECK")
    # print("select pattern is: {}".format(select_pattern))
    # print("from pattern is: {}".format(from_pattern))
    # print("where pattern is: {}".format(where_pattern))
    # print("group by pattern is: {}".format(group_by_pattern))
    # print("order by pattern is: {}".format(order_by_pattern))




    # Find the matches for each clause
    select_match = select_pattern.search(sql_query)
    from_match = from_pattern.search(sql_query)
    where_match = where_pattern.search(sql_query)
    group_by_match = group_by_pattern.search(sql_query)
    order_by_match = order_by_pattern.search(sql_query)

    # print("2nd CHECK")
    # print("select match is: {}".format(select_match))
    # print("from match is: {}".format(from_match))
    # print("where match is: {}".format(where_match))
    # print("group by match is: {}".format(group_by_match))
    # print("order by match is: {}".format(order_by_match))




    # Create the dictionaries for each clause
    # select_dict = {}
    # from_dict = {}
    # where_dict = {}
    # group_by_dict = {}
    # order_by_dict = {}


    # Create the dictionary for 1st query
    dict = {}

    # print("3rd CHECK")
    # print(dict)


    # print("where_match is this: {}".format(where_match))
    # print("type of where_match: {}".format(type(where_match)))

    # where_match_string = where_match.group(1)
    # print("where_match_string is this: {}".format(' '.join(where_match_string.splitlines())))
    # print("IT ENDS HERE")


    # print("3rd CHECK")
    # print("select_dict is: {}".format(select_dict))
    # print("from_dict is: {}".format(from_dict))
    # print("where_dict is: {}".format(where_dict))
    # print("group_by_dict is: {}".format(group_by_dict))
    # print("order_by_dict is: {}".format(order_by_dict))






    # if where_match:
    #     where_clause = where_match.group(1).strip().split('and')

    #     #print("Before: {}".format(where_clause))
    #     #print(type(where_clause))

    #     for i in range(len(where_clause)):
    #         where_clause[i] = " ".join(where_clause[i].split())

    #     #print("After: {}".format(where_clause))

    #     dict['WHERE'] = where_clause


    










    # If a match was found, split the clause into its components and add them to the dictionary
    if select_match:
        select_clause = select_match.group(1).strip().split(',')

        for i in range(len(select_clause)):
            select_clause[i] = select_clause[i].strip()

        dict['SELECT'] = select_clause
        
    if from_match:
        from_clause = from_match.group(1).strip().split(',')
        
        for i in range(len(from_clause)):
            from_clause[i] = from_clause[i].strip()
        
        dict['FROM'] = from_clause

    if where_match:
        where_clause = where_match.group(1).strip().split('and')

        for i in range(len(where_clause)):
            where_clause[i] = " ".join(where_clause[i].split())

        dict['WHERE'] = where_clause

    if group_by_match:
        group_by_clause = group_by_match.group(1).strip().split(',')

        for i in range(len(group_by_clause)):
            group_by_clause[i] = group_by_clause[i].strip()
        
        dict['GROUP BY'] = group_by_clause

    if order_by_match:
        order_by_clause = order_by_match.group(1).strip().split(',')

        for i in range(len(order_by_clause)):
            order_by_clause[i] = order_by_clause[i].strip()

        dict['ORDER BY'] = order_by_clause




    # print("4th CHECK")
    # print('Dictionary of clauses and predicates for Query 1 is: \n{}'.format(dict))

    return dict 





query_1_dict = parse_sql_file('C:/Users/user/Desktop/CZ4031/Project 2/2.sql')

print('Final Check and Result:')
print('Dictionary for Query 1 is: \n{}'.format(query_1_dict))






















































