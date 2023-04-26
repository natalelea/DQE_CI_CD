from conf_new import conn
cursor = conn.cursor(as_dict=True)

def test_check_max_salary_value():
    """
    Name: Verifying if salary range is eligible
    Steps: 1. Getting maximum value of [salary] column from [hr].[employees]
           2. Comparing if the result value is in expected range which is less then 50K
    Expected result: True
    """
    cursor.execute('SELECT max([salary]) as max_sal FROM [TRN].[hr].[employees]')
    for row in cursor:
        result = row['max_sal']
    assert result < 50000
