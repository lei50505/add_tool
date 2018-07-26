#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''doc'''
# pylint:disable=too-many-branches,too-many-statements,too-many-locals,broad-except

import time
import traceback

class File():
    '''doc'''
    def __init__(self, path):
        self.path = path
    def read_nums(self):
        '''doc'''
        file_oper = open(self.path)
        lines = file_oper.readlines()
        ret_lines = []
        for line in lines:
            ret_lines.append(float(line.strip()))
        return ret_lines
def main():
    '''doc'''
    in_file = File("in.txt")
    nums = in_file.read_nums()
    bbb=nums[0]
    out_file = open("out.txt","w")
    out_lines=[]


    for i in range(1,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == bbb:
                print(nums[i],nums[j])
                out_lines.append("%f %f \r\n" % (nums[i],nums[j]))
                break

    for i in range(1,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] == bbb:
                    print(nums[i],nums[j],nums[k])
                    out_lines.append("%f %f %f \r\n" % (nums[i],nums[j],nums[k]))
                    break

    for i in range(1,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for a in range(k+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]+nums[a] == bbb:
                        print(nums[i],nums[j],nums[k],nums[a])
                        out_lines.append("%f %f %f %f \r\n" % (nums[i],nums[j],nums[k],nums[a]))
                        break
    for i in range(1,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for a in range(k+1,len(nums)):
                    for b in range(a+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[a]+nums[b] == bbb:
                            print(nums[i],nums[j],nums[k],nums[a],nums[b])
                            out_lines.append("%f %f %f %f %f \r\n" % (nums[i],nums[j],nums[k],nums[a] ,nums[b]))
                            break
    out_file.writelines(out_lines)
    print("处理成功")


if __name__ == "__main__":
    try:
        main()
        print("2秒后退出")
        time.sleep(2)
    except Exception:
        print(traceback.format_exc())
        print("10秒后退出")
        time.sleep(10)
