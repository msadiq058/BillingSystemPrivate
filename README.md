# Billing System

## Use Case
Store daily sales record having fields like <br/>
firm_name , date , quantity , size of product.<br/>

Generate bills by firm_name , start_date and end_date <br/>

## Working of Project
### To store daily sales record.<br/>
Records are entered via the Django Admin Page.Database used is sql.<br/>
Records are stored in the table with various data fields.<br/>
<br/>

### To generate bills
The data fields like firm_name and date is inserted by user.</br>
Data is fecthed from the sql table according to the data fields.<br>
Data is then summarised to make a summary table about the sales.<br>
Both the summary sheet and the detailed sheet is transferred to an excel file.<br>
