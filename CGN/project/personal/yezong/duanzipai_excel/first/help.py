import xlwt
import winreg
info=[['3LKA1001CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 19*1.5', 'K3', 'A', 'OR'], ['3LKA1002CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA2821ZRE', '3LKA1101TR-', 'C 4*6', 'K3', 'A', 'OR'], ['3LKA1003CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 7*1.5', 'K3', 'A', 'OR'], ['3LKA1004CAC', '3BSA2821ZRE', '3LGM1101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 7*1.5', 'K3', 'A', 'OR'], ['3LKA1005CAC', '3BSA2824ZRE', '3LAA3101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1006CAC', '3BSA2824ZRE', '3LVA3301TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1007CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA2821ZRE', '3LGM1101TB-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1008CAC', '3BSA2821ZRE', '3LGM1101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1009CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA2821ZRE', '3RCP1101TB-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1010CAC', '3BSA2821ZRE', '3LKA1101TB-', '3BSA2821ZRE', '3RCP1401TB-', 'C 4*1.5', 'K3', 'A', 'OR'], ['3LKA1001CAM', '3BSA2821ZRE', '3LKA1101TR-', '3BSA3621ZRE', '3KCP1001AR-', 'M 8*2*1.0', 'K3', 'A', 'OR'], ['3LKA1002CAM', '3BSA2821ZRE', '3LKA1101TB-', '3BSA3621ZRE', '3KCP1001AR-', 'M 2*2*1.0', 'K3', 'A', 'OR']]




class excel_writer():
    def __init__(self,info=None):
        self.info=info
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('电缆信息')
        worksheet.write(0, 0, label='电缆名')
        worksheet.write(0, 1, label='起始房间号')
        worksheet.write(0, 2, label='起始设备')
        worksheet.write(0, 3, label='终止房间号')
        worksheet.write(0, 4, label='终止设备')
        worksheet.write(0, 5, label='电缆规格')
        worksheet.write(0, 6, label='鉴定等级')
        worksheet.write(0, 7, label='列别')
        worksheet.write(0, 8, label='颜色')
        worksheet.write(0, 9, label='安全等级')
        self.path=self.get_desktop()
        for i in range(len(info)):
            for j in range(len(info[i])):
                worksheet.write(i+1,j,info[i][j])
            worksheet.write(i+1,len(info[i]),"FC3")
        workbook.save(self.path+'\\cable_test.xls')

    def get_desktop(self):

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )

        return winreg.QueryValueEx(key, "Desktop")[0]



ew=excel_writer(info)