import re


# This function parses a query and returns a dictionary with each of the clauses and its predicates as a key-value pair
def parse_sql_query(input):

    sql_query = input

    # Open the file and read its contents
    #with open(file_path, 'r') as file:
    #    sql_query = file.read()

    #sql_query = "select returnflag, linestatus, sum(linequantity) as sumqty, count(*) as count_order from table where blah1 and blah4 and blah5 group by blah 2 order by blah 3"

    #sql_query = "select blah1, blah2 from blah3, blah4 where blah5 and blah6 and blah7 group by blah8, blah9 having blah10 order by blah11 limit blah12"


    # sql_query = "select\
    #     blah1,\
    #     blah2\
    # from\
    #     blah3,\
    #     blah4\
    # where\
    #     blah5\
    #     and blah6\
    #     and blah7\
    # group by\
    #     blah8,\
    #     blah9\
    # having\
    #     blah10\
    # order by\
    #     blah11\
    # limit\
    #     blah12\
    # "


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
    #             blah1 = blah2 \
    #     )\
    #     and s_nationkey = n_nationkey\
    #     and n_name = ':3'\
    # group by\
    #     s_name\
    # order by\
    #     lastoneee;\
    # "


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

    # Order of SQL clauses
    # select -- only this
    # from   -- and this are mandatory clauses
    # where
    # group by
    # having  -- not in yet
    # order by
    # limit  -- not in yet


    # Assumptions and preconditions
    # 1. Queries written with accurate clause order, ....
    # 2. Queries only use these common clauses ...
    # 3. Clauses are all written in lower cases

    # Define regular expressions to match each clause
    # select_pattern = re.compile(r'select (.+?) from', re.DOTALL)
    # from_pattern = re.compile(r'from (.+?) (?: where|group by|order by|$)', re.DOTALL)
    # where_pattern = re.compile(r'where (.+?) (?: group by|order by|$)', re.DOTALL)
    # group_by_pattern = re.compile(r'group by (.+?) (?: order by|$)', re.DOTALL)
    # order_by_pattern = re.compile(r'order by (.+?) $', re.DOTALL)
    


    select_pattern = re.compile(r'select (.+?) from', re.DOTALL)
    from_pattern = re.compile(r'from (.+?) (?: where|group by|having|order by|limit|$)', re.DOTALL)
    where_pattern = re.compile(r'where (.+?) (?: group by|having|order by|limit|$)', re.DOTALL)
    group_by_pattern = re.compile(r'group by (.+?) (?: having|order by|limit|$)', re.DOTALL)
    having_pattern = re.compile(r'having (.+?) (?: order by|limit|$)', re.DOTALL)
    order_by_pattern = re.compile(r'order by (.+?) (?: limit|$)', re.DOTALL)
    limit_pattern = re.compile(r'limit (.+?) $', re.DOTALL)

    print("CHECK 1: {}".format(from_pattern))
    print("CHECK 1: {}".format(where_pattern))


    # Find the matches for each clause
    select_match = select_pattern.search(sql_query)
    from_match = from_pattern.search(sql_query)
    where_match = where_pattern.search(sql_query)
    group_by_match = group_by_pattern.search(sql_query)
    having_match = having_pattern.search(sql_query)
    order_by_match = order_by_pattern.search(sql_query)
    limit_match = limit_pattern.search(sql_query)

    print("CHECK 2: {}".format(from_match))
    print("CHECK 2: {}".format(where_match))

    # Initialise dictionary for the query
    dict = {}

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

    if having_match:
        having_clause = having_match.group(1).strip().split(',')

        for i in range(len(having_clause)):
            having_clause[i] = having_clause[i].strip()
        
        dict['HAVING'] = having_clause
    
    
    if order_by_match:
        order_by_clause = order_by_match.group(1).strip().split(',')

        for i in range(len(order_by_clause)):
            order_by_clause[i] = order_by_clause[i].strip()

        dict['ORDER BY'] = order_by_clause
    
    if limit_match:
        limit_clause = limit_match.group(1).strip().split(',')

        for i in range(len(limit_clause)):
            limit_clause[i] = limit_clause[i].strip()

        dict['LIMIT'] = limit_clause


    return dict 


query_1_dict = parse_sql_query('C:/Users/user/Desktop/CZ4031/Project 2/2.sql')

print('Final Check and Result:')
print('Dictionary for Query 1 is: \n{}'.format(query_1_dict))










if __name__ == "__main__":

    # input1 and input2 should be taken from front-end user input, presumably same input for the qep generation
    input1 = "select\
        c_custkey,\
        c_name,\
        sum(l_extendedprice * (1 - l_discount)) as revenue,\
        c_acctbal,\
        n_name,\
        c_address,\
        c_phone,\
        c_comment\
    from\
        customer,\
        orders,\
        lineitem,\
        nation\
    where\
        c_custkey = o_custkey\
        and l_orderkey = o_orderkey\
        and o_orderdate >= date ':1'\
        and o_orderdate < date ':1' + interval '3' month\
        and l_returnflag = 'R'\
        and c_nationkey = n_nationkey\
    group by\
        c_custkey,\
        c_name,\
        c_acctbal,\
        c_phone,\
        n_name,\
        c_address,\
        c_comment\
    order by\
        revenue desc;\
    "

    input2 = "select\
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
    
    # Creation of dictionary for each query
    query_1_dict = parse_sql_query(input1)
    query_2_dict = parse_sql_query(input2)

    print('Final Output:')
    print('Dictionary for Query 1 is: \n{}'.format(query_1_dict))
    print("\n")
    print('Dictionary for Query 2 is: \n{}'.format(query_2_dict))

    















































