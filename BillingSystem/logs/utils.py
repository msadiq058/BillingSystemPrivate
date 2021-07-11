import xlsxwriter
import datetime,os

def generateExcel(data,name,start_date,end_date):
    # data = [ for i in data]
    start_date = start_date.strftime("%d-%m-%Y")
    end_date = end_date.strftime("%d-%m-%Y")
    print(os.getcwd())
    # os.geth
    folder_path = os.getcwd()+"/bills"
    try:
        os.mkdir(folder_path)
        print("Build directory successfully.")
    except:
        print("Directory already present.")
    file_name = "Invoice_"+str(name)+"_"+str(start_date)+"_"+str(end_date)+".xlsx"
    

    # print(file_name)
    
    file_name_var = 1
    file_name_len = len(file_name)-5
    while(file_name in os.listdir(folder_path)):
        file_name = file_name[:file_name_len]+"("+str(file_name_var)+")"+".xlsx"
        print(file_name)
        file_name_var+=1

    file_path = os.path.join(folder_path,file_name)
    print(file_path)
    workbook = xlsxwriter.Workbook(filename=file_path)
    generateSummary(workbook,name,data,start_date,end_date)
    enterDetailWorksheet(workbook,name,data)
    workbook.close()

def enterDetailWorksheet(workbook,name,data):

    row ,col ,sr_no = 0,0,1
    worksheet_details = workbook.add_worksheet("Detailed Information")
    
    bold = workbook.add_format({'bold':True,'center_across':True,'border':1})
    worksheet_details.write(row,0,"Sr No.",bold)
    worksheet_details.write(row,1,"Date",bold)
    worksheet_details.write(row,2,"Size",bold)
    worksheet_details.write(row,3,"QTY",bold)
    worksheet_details.write(row,4,"Weight",bold)
    worksheet_details.write(row,5,"Making Type",bold)
    worksheet_details.write(row,6,"Remarks",bold)
    row+=1

    worksheet_details.set_column('A:A',6)
    worksheet_details.set_column('B:B',10)
    worksheet_details.set_column('C:C',5)
    worksheet_details.set_column('D:D',7)
    worksheet_details.set_column('E:E',10)
    worksheet_details.set_column('F:F',13)
    worksheet_details.set_column('G:G',12)

    border = workbook.add_format({'border':1})
    border_and_mid = workbook.add_format({'border':1,'center_across':True})
    for entry in data:
        date = entry.date.strftime("%d-%m-%Y")
        size = entry.size
        weight = entry.weight
        quantity = entry.quantity
        making_type = entry.making_type
        remarks = entry.remarks
        worksheet_details.write(row,col+0,sr_no,border_and_mid)
        worksheet_details.write(row,col+1,date,border)
        worksheet_details.write(row,col+2,size,border_and_mid)
        worksheet_details.write(row,col+3,quantity,border)
        worksheet_details.write(row,col+4,weight,border)
        worksheet_details.write(row,col+5,making_type,border_and_mid)
        worksheet_details.write(row,col+6,remarks,border)
        row+=1
        sr_no +=1


def generateSummary(workbook,name,data,start_date,end_date):
    worksheet_summary = workbook.add_worksheet("Summary")
    row ,col = 0,0
    weight_sticked = []
    weight_framed = []
    quantity_sticked = []
    quantity_framed = []
    for i in range(8):
        weight_sticked.append(0.0)
        quantity_sticked.append(0)

        weight_framed.append(0.0)
        quantity_framed.append(0)

    size_to_index = {
        '1.0':0,
        '1.5':1,
        '2.0':2,
        '2.5':3,
        '3.0':4,
        '4.0':5,
        '5.0':6,
        '6.0':7
    }
    index_to_size={
        0:'1.0',
        1:'1.5',
        2:'2.0',
        3:'2.5',
        4:'3.0',
        5:'4.0',
        6:'5.0',
        7:'6.0',
    }
    for entry in data:
        # print(entry.size,(entry.size))
        if entry.making_type=='Framed':
            weight_framed[size_to_index[entry.size]] += float(entry.weight)
            quantity_framed[size_to_index[entry.size]] += int(entry.quantity)
        else:
            weight_sticked[size_to_index[entry.size]] += float(entry.weight)
            quantity_sticked[size_to_index[entry.size]] += int(entry.quantity)

    row ,col,sr_no = 0,0,1


    merge_format = workbook.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'center'
    })

    # start_date = start_date.strftime("%d-%m-%Y")
    # end_date = end_date.strftime("%d-%m-%Y")

    border = workbook.add_format({'border':1})
    border_and_mid = workbook.add_format({'border':1,'center_across':True})
    bold = workbook.add_format({'bold':True,'center_across':True,'border':1})

    
    worksheet_summary.merge_range('C1:D1',str(name),merge_format)

    row+=2
    worksheet_summary.merge_range('A3:B3','Start Date',bold)
    worksheet_summary.write(row,2,start_date,border)
    worksheet_summary.write(row,4,'End Date',bold)
    worksheet_summary.write(row,5,end_date,border)

    row+=2

    worksheet_summary.write(row,0,"Sr No.",bold)
    worksheet_summary.write(row,1,"Size",bold)
    worksheet_summary.write(row,2,"Quantity",bold)
    worksheet_summary.write(row,3,"Weight",bold)
    worksheet_summary.write(row,4,"Type",bold)
    worksheet_summary.write(row,5,"Rate(QTY)",bold)
    worksheet_summary.write(row,6,"Rate(Weight)",bold)
    worksheet_summary.write(row,7,"Total(QTY)",bold)
    worksheet_summary.write(row,8,"Total(Weight)",bold)
    worksheet_summary.write(row,9,"Total",bold)
    
    worksheet_summary.set_column('A:A',6)
    worksheet_summary.set_column('B:B',5)
    worksheet_summary.set_column('C:C',10)
    worksheet_summary.set_column('D:D',10)
    worksheet_summary.set_column('E:E',8)
    worksheet_summary.set_column('E:E',11)
    worksheet_summary.set_column('F:F',12)
    worksheet_summary.set_column('G:G',11)
    worksheet_summary.set_column('H:H',12)

    row+=1
    for i in range(0,8):
        if weight_framed[i]!=0 :
            worksheet_summary.write(row,col+0,sr_no,border_and_mid)
            worksheet_summary.write(row,col+1,index_to_size[i],border_and_mid)
            worksheet_summary.write(row,col+2,quantity_framed[i],border)
            worksheet_summary.write(row,col+3,weight_framed[i],border)
            worksheet_summary.write(row,col+4,'Framed',border)
            # worksheet_summary.write(row,col+5,0,border)
            # worksheet_summary.write(row,col+6,0,border)
            # worksheet_summary.write(row,col+7,0,border)

            row+=1
            sr_no+=1
    
    for i in range(0,8):
        if weight_sticked[i]!=0 :
            worksheet_summary.write(row,col+0,sr_no,border_and_mid)
            worksheet_summary.write(row,col+1,index_to_size[i],border_and_mid)
            worksheet_summary.write(row,col+2,quantity_sticked[i],border)
            worksheet_summary.write(row,col+3,weight_sticked[i],border)
            worksheet_summary.write(row,col+4,'Sticked',border)
            # worksheet_summary.write(row,col+5,0,border)
            # worksheet_summary.write(row,col+6,0,border)
            
            row+=1
            sr_no+=1
    
    row+=1


    worksheet_summary.write(row,1,'Total',)