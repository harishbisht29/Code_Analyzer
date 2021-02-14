/*
Sample Libname Statement
*/
Libname        test 'This is a test data';
/*
Sample Include Statement
*/
%Include "/user/bin/sas/sample_program.sas";

/*Sample Data Step*/
Data _Null_;



    Value= "name";
Run;

/*Sample Proc Step
*/
Proc Sql;
    Create table test 
    as select * from test1 a inner join test2 b on a.name=b.name 
    left outer join test3 c on c.name=a.name 
    order by name;
Run;