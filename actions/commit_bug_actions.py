# 提交bug业务类

# 业务封装思路1：
class CommitBugActions(object):
    def commit_bug(self, bug_title, bug_content):
        pass

    def commit_bug02(self, **bug_info):
        pass


CommitBugActions.commit_bug(bug_title='new_p5', bug_content='')


# 业务封装思路2：封装成函数
def commit_bug(self, bug_title, bug_content):
    pass


def commit_bug_02(self, **bug_info):
    pass


commit_bug(bug_title='new_p5', bug_content='')
