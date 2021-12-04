def stu_name(className, *stus):
    print("班级名称：", className)
    for s in stus:
        print(stus)


stu_name("P5班", "wujinshu")
stu_name("P5班", "wujinshu", "lisi")


# id = frameid  name = framename  element=element_info
def switch_to_frame(**element_dict):
    for key in element_dict.keys():
        print(key, element_dict[key])


switch_to_frame(id="main_frameid")
