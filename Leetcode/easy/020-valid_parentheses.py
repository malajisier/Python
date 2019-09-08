class solution:
    def is_valid(self, s):
        # 加？，防止栈空报错和 第一个为右括号 报错
        dic = {'{':'}', '[':']', '(':')', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        # 判断是否是有效括号组合，（只剩未出栈的左括号的情况）
        return len(stack) == 1


# https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
#