import tkinter as tk, os, time, sys

print(sys.getdefaultencoding())

root_path = r'N:\loveNN\2019下半年主要工作'
nation_question = r'N:\loveNN\2019下半年主要工作\National_Questions国内问题'
overseas_question = r'N:\loveNN\2019下半年主要工作\Overseas_Question海外问题'
patch_task = r'N:\loveNN\2019下半年主要工作\paths补丁&需求处理'
other_common = r'N:\loveNN\2019下半年主要工作\otherThing其他公共事务'

record_question = '问题录入，格式如：【陕西电信】【SR 1137689】入局呼叫甄别失败问题'

questions_description, select_path = '', ''

directory_choice = [
        # (root_path, 0),
        (nation_question, 0),
        (overseas_question, 1),
        (patch_task, 2),
        (other_common, 3),
    ]

# document path #
CPI_document = r'C:\Users\l00382665\Desktop\lovline_nana\HUAWEI UAC3000 接入网关控制器 产品文档-(V100R019C00_01).chm'
GPI_document = r'C:\Users\l00382665\Desktop\lovline_nana\HUAWEI UAC3000 接入网关控制器 GTS产品文档(GPI)-(V100R018C10_02).chm'

# execute program path #
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
ie_path = r'C:\Program Files\Internet Explorer\iexplore.exe'
notepad_path = r'D:\Notepad++\notepad++.exe'
eDiary_path = r'D:\eDiary-3.3\eDiary.exe'
eSpace_path = r'C:\Program Files (x86)\eSpace_Desktop\eSpace.exe'
outlook_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Outlook 2013'
iLMT_path = r'D:\HW iLMT\omu\workspace1\client\lmt_client.exe'
source_insight_path = r'C:\Program Files (x86)\Source Insight 3\Insight3.exe'
RDO_path = r'C:\Program Files (x86)\Remote Desktop Organizer\RDO.exe'
pycharm_path = r'C:\Program Files\JetBrains\PyCharm 2017.1.5\bin\pycharm64.exe'

# directory path #
desktop_path = r'C:\Users\l00382665\Desktop'
lovline_path = r'C:\Users\l00382665\Desktop\lovline_nana'
work_path = r'N:\loveNN\2019下半年主要工作'
work_national_path = r'N:\loveNN\2019下半年主要工作\National_Questions国内问题'
work_patch_path = r'N:\loveNN\2019下半年主要工作\paths补丁&需求处理'
work_oversea_path = r'N:\loveNN\2019下半年主要工作\Overseas_Question海外问题'

open_execute_file_list = [
    CPI_document,
    GPI_document,
    chrome_path,
    ie_path,
    notepad_path,
    eDiary_path,
    eSpace_path,
    outlook_path,
    iLMT_path,
    source_insight_path,
    source_insight_path,
    RDO_path,
    desktop_path,
    lovline_path,
    work_path,
    work_national_path,
    work_national_path,
    work_patch_path,
    work_oversea_path,
]


def start_execute():
    global open_execute_file_list
    for path in open_execute_file_list:
        os.startfile(path)
        time.sleep(0.7)
    window.quit()


window = tk.Tk()
window.title('One-click Open')
window.geometry('300x100')

tk.Label(window, textvariable='', width='27').pack()
tk.Button(window, text="open common program", height='2', width='20', font=('black', 12), command=start_execute,
           bg='#FFFAFA', fg='#4F4F4F', activebackground='white', relief='raised').pack()


window.mainloop()
