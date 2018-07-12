import sys
import re
import copy


class DiffCommands:
    def __init__(self, filename):
        self.name = filename
        self.file = open(filename)
        self.text = self.file.read().splitlines()
        line_by_readlines = open(filename).readlines()
        for x in line_by_readlines:
            if ' ' in x or 'D' in x or 'A' in x or 'C' in x or (x == '\n'):
##            if not(re.match('^(\d+)(?:,(\d+))?d(\d+)\n$|^(\d+)a(\d+)(?:,(\d+))?\n$|^(\d+)(?:,(\d+))?c(\d+)(?:,(\d+))?\n$',x)):
                raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                sys.exit()
            if 'd' in x:
                if len(re.findall('[0-9]\d*', x)) > 3:
                    raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                    sys.exit()

    def __str__(self):
        for x in self.text:
            if x == self.text[-1]:
                return self.text[-1]
            print(x)

class DiffCommandsError(Exception):
    def __init__(self, message):
        self.message = message


class OriginalNewFiles:
    def __init__(self, file1, file2):
        self.name1, self.name2 = file1, file2
        self.file1, self.file2 = open(file1), open(file2)
        self.text1, self.text2 = self.file1.read().splitlines(), self.file2.read().splitlines()
        
        self.mapping = dict()
        self.LCS_all = self._FindAllLCS(self.mapping, self._LCS(self.text1 ,self.text2),
                                        self.text1 ,self.text2, len(self.text1), len(self.text2))[0]
        self.LCS_one = self._FindOneLCS(self._LCS(self.text1 ,self.text2), self.text1 ,self.text2)
        self.backall = self._backTrackAll(self._LCS(self.text1 ,self.text2) , self.text1 ,self.text2,
                                          len(self.text1), len(self.text2))

    def __str__(self, diffs):
        for x in diffs:
            if x == diffs[-1]:
                return diffs[-1]
            print(x)

    def _LCS(self, X, Y):
        m = len(X)
        n = len(Y)
        C = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]: 
                    C[i][j] = C[i-1][j-1] + 1
                else:
                    C[i][j] = max(C[i][j-1], C[i-1][j])
        return C

    def _FindOneLCS(self, L, m, n):
        LCS_one = ['...' for i in range(len(m))]
        i, j = len(m) - 1, len(n) - 1
        while i> 1 or j >= 1:
            if m[i] == n[j]:
                LCS_one[i] = m[i]
                i -= 1
                j -= 1
            else:
                if L[i][j-1] >= L[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        return LCS_one

    def _FindAllLCS(self, lcs_dict, mat, list1, list2, index1, index2):
        if (index1, index2) in lcs_dict:
            return lcs_dict[(index1, index2)]
        if index1 == 0 or index2 == 0:
            return [[]]
        if list1[index1 - 1] == list2[index2 - 1]:
            lcs_dict[(index1, index2)] = [prevs + [list1[index1 - 1]] for prevs in self._FindAllLCS(lcs_dict, mat, list1, list2, index1 - 1, index2 - 1)]
            return lcs_dict[(index1, index2)]
        else:
            lcs_list = []
            if mat[index1][index2 - 1] >= mat[index1 - 1][index2]:
                before = self._FindAllLCS(lcs_dict, mat, list1, list2, index1, index2 - 1)
                for series in before:
                    if not series in lcs_list:
                        lcs_list.append(series)
            if mat[index1 - 1][index2] >= mat[index1][index2 - 1]:
                before = self._FindAllLCS(lcs_dict, mat, list1, list2, index1 - 1, index2)
                for series in before:
                    if not series in lcs_list:
                        lcs_list.append(series)
            lcs_dict[(index1, index2)] = lcs_list
            return lcs_list

    def _backTrackAll(self, C, X, Y, i, j):
        if i == 0 or j == 0:
            return set([""])
        elif X[i-1] == Y[j-1]:
            return set([Z + X[i-1] for Z in self._backTrackAll(C, X, Y, i-1, j-1)])
        else:
            R = set()
            if C[i][j-1] >= C[i-1][j]:
                R.update(self._backTrackAll(C, X, Y, i, j-1))
            if C[i-1][j] >= C[i][j-1]:
                R.update(self._backTrackAll(C, X, Y, i-1, j))
            return R
    
    def output_diff(self, diff_N):
        for x in diff_N.text:
            if 'd' in x:
                Head = x[0: x.index('d')]
                print(x)
                if Head.isdigit():
                    print('< {}'.format(self.text1[int(Head) - 1]))
                else:
                    D1, D2 = int(re.findall('[0-9]\d*', Head)[0]), int(re.findall('[0-9]\d*', Head)[1])
                    for i in range(D1, D2+1):
                        print('< {}'.format(self.text1[i - 1]))
            elif 'a' in x:
                List = x[x.index('a') + 1:]
                print(x)
                if List.isdigit():
                    print('> {}'.format(self.text2[int(List) - 1]))
                else:
                    D1, D2 = int(re.findall('[0-9]\d*', List)[0]), int(re.findall('[0-9]\d*', List)[1])
                    for i in range(D1, D2+1):
                        print('> {}'.format(self.text2[i - 1]))
            elif 'c' in x:
                Head = x[0: x.index('c')]
                List = x[x.index('c') + 1:]
                print(x)
                if Head.isdigit():
                    print('< {}'.format(self.text1[int(Head) - 1]))
                    print('---')
                    print('> {}'.format(self.text2[int(List) - 1]))
                else:
                    D1, D2 = int(re.findall('[0-9]\d*', Head)[0]), int(re.findall('[0-9]\d*', Head)[1])
                    D3, D4 = int(re.findall('[0-9]\d*', List)[0]), int(re.findall('[0-9]\d*', List)[1])
                    for i in range(D1, D2+1):
                        print('< {}'.format(self.text1[i - 1]))
                    print('---')
                    for i in range(D3, D4+1):
                        print('> {}'.format(self.text2[i - 1]))


    def output_unmodified_from_original(self, diff_N):
        print(self.LCS_one[0])
        for a in range(1, len(self.LCS_one)):
            if self.LCS_one[a] == '...':
                if self.LCS_one[a-1] != '...':
                    print(self.LCS_one[a])
            else:
                print(self.LCS_one[a])

    def output_unmodified_from_new(self, diff_N):
        Copy2 = copy.deepcopy(self.text2)
        for x in diff_N.text:
            if 'a' in x:
                List = x[x.index('a') + 1:]
                if List.isdigit():
                    Copy2[int(List)-1] = '...'
                else:
                    D1, D2 = int(re.findall('[0-9]\d*', List)[0]), int(re.findall('[0-9]\d*', List)[1])
                    for i in range(D1, D2+1):
                        Copy2[i-1]='...'
            if 'c' in x:
                List = x[x.index('c') + 1:]
                if List.isdigit():
                    Copy2[int(List)-1] = '...'
                else:
                    D1, D2 = int(re.findall('[0-9]\d*', List)[0]), int(re.findall('[0-9]\d*', List)[1])
                    for i in range(D1, D2+1):
                        Copy2[i-1]='...'
        print(Copy2[0])
        for a in range(1, len(Copy2)):
            if Copy2[a] == '...':
                if Copy2[a - 1] != '...':
                    print(Copy2[a])
            else:
                print(Copy2[a])

    def get_all_diff_commands(self):
        ALL_Diff = ['']
        for L in range(len(self.LCS_all)):
            index1 = self.text1.index(self.LCS_all[L])
            index1_last = self.text1.index(self.LCS_all[L-1])
            index2 = self.text2.index(self.LCS_all[L])
            index2_last = self.text2.index(self.LCS_all[L-1])
            if L == 0:
                if index1 == 0 and index2 > 0:
                    if index2 == 1:
                        ALL_Diff[0]+=('0a1\n')
                    else:
                        ALL_Diff[0]+=('0a1,{}\n'.format(index2))
                elif index1 > 0 and index2 == 0:
                    if index1 == 1:
                        ALL_Diff[0]+=('1d0\n')
                    else:
                        ALL_Diff[0]+=('1,{}d0\n'.format(index1))
                elif index1 > 0 and index2 > 0:
                    if index1 == 1 and index2 == 1:
                        ALL_Diff[0]+=('1c1\n')
                    elif index1 == 1 and index2 > 1:
                        ALL_Diff[0]+=('1c1,{}\n'.format(index2))
                    elif index1 > 1 and index2 == 1:
                        ALL_Diff[0]+=('1,{}c1\n'.format(index1))
                    else:
                        ALL_Diff[0]+=('1,{}c1,{}\n'.format(index1, index2))
                elif index1 == 0 and index2 == 0:
                    if index1 == len(self.text1) - 1 and index2 < len(self.text2) - 1:
                        if len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{}a{}\n'.format(index1 + 1, index2 + 2))
                        else:
                            ALL_Diff[0]+=('{}a{},{}\n'.format(index1 + 1, index2 + 2, len(self.text2)))
                    elif index1 < len(self.text1) - 1 and index2 == len(self.text2) - 1:
                        if len(self.text1) - 1 - index1 == 1:
                            ALL_Diff[0]+=('{}d{}\n'.format(index1 + 2, index2 + 1))
                        else:
                            ALL_Diff[0]+=('{},{}d{}\n'.format(index1 + 2, len(self.text1), index2 + 1))
                    elif index1 < len(self.text1) - 1 and index2 < len(self.text2) - 1:
                        if len(self.text1) - 1 - index1 == 1 and len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{}c{}\n'.format(index1 + 2, index2 + 2))
                        elif len(self.text1) - 1 - index1 > 1 and len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{},{}c{}\n'.format(index1 + 2, len(self.text1), index2 + 2))
                        else:
                            ALL_Diff[0]+=('{},{}c{},{}\n'.format(index1 + 2, len(self.text1), index2 + 2, len(self.text2)))
                continue
            else:
                if index1 - index1_last == 1 and index2 - index2_last > 1:
                    if index2 - index2_last == 2:
                        ALL_Diff[0]+=('{}a{}\n'.format(index1_last + 1, index2_last + 2))
                        continue
                    elif index2 - index2_last > 2:
                        ALL_Diff[0]+=('{}a{},{}\n'.format(index1_last + 1, index2_last + 2, index2))
                        continue
                elif index1 - index1_last > 1 and index2 - index2_last == 1:
                    if index1 - index1_last == 2:
                        ALL_Diff[0]+=('{}d{}\n'.format(index1_last + 2, index2_last + 1))
                        continue
                    elif index1 - index1_last > 2:
                        ALL_Diff[0]+=('{},{}d{}\n'.format(index1_last + 2, index1, index2_last + 1))
                        continue
                elif index1 - index1_last > 1 and index2 - index2_last > 1:
                    if index1 - index1_last == 2 and index2 - index2_last == 2:
                        ALL_Diff[0]+=('{}c{}\n'.format(index1_last + 2, index2_last + 2))
                        continue
                    elif index1 - index1_last > 2 and index2 - index2_last == 2:
                        ALL_Diff[0]+=('{},{}c{}\n'.format(index1_last + 2, index1, index2_last + 2))
                        continue
                    elif index1 - index1_last > 2 and index2 - index2_last > 2:
                        ALL_Diff[0]+=('{},{}c{},{}\n'.format(index1_last + 2, index1, index2_last + 2, index2))
                        continue
                if L == len(self.LCS_all) - 1:
                    if index1 == len(self.text1) - 1 and index2 < len(self.text2) - 1:
                        if len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{}a{}\n'.format(index1 + 1, index2 + 2))
                        else:
                            ALL_Diff[0]+=('{}a{},{}\n'.format(index1 + 1, index2 + 2, len(self.text2)))
                    elif index1 < len(self.text1) - 1 and index2 == len(self.text2) - 1:
                        if len(self.text1) - 1 - index1 == 1:
                            ALL_Diff[0]+=('{}d{}\n'.format(index1 + 2, index2 + 1))
                        else:
                            ALL_Diff[0]+=('{},{}d{}\n'.format(index1 + 2, len(self.text1), index2 + 1))
                    elif index1 < len(self.text1) - 1 and index2 < len(self.text2) - 1:
                        if len(self.text1) - 1 - index1 == 1 and len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{}c{}\n'.format(index1 + 2, index2 + 2))
                        elif len(self.text1) - 1 - index1 > 1 and len(self.text2) - 1 - index2 == 1:
                            ALL_Diff[0]+=('{},{}c{}\n'.format(index1 + 2, len(self.text1), index2 + 2))
                        else:
                            ALL_Diff[0]+=('{},{}c{},{}\n'.format(index1 + 2, len(self.text1), index2 + 2, len(self.text2)))
        ALL_Diff[0] = ALL_Diff[0][0:-1]
        A = int(re.findall('[0-9]\d*', self.name1)[0])
        if A > 1:
            for i in range(A - 1):
                ALL_Diff.append(ALL_Diff[0])
        return ALL_Diff



    def is_a_possible_diff(self, diff_N):
        if int(re.findall('[0-9]\d*', diff_N.name)[0]) == int(re.findall('[0-9]\d*', self.name1)[0]):
            return True
        else:
            return False

##        num = 0
##        Copy = copy.deepcopy(self.text1)
##        for x in diff_N.text:
##            if 'd' in x:
##                Head = x[0: x.index('d')]
##                if Head.isdigit():
##                    Copy.pop(int(Head)-1+num)
##                    num -= 1
##                else:
##                    D1, D2 = int(re.findall('[0-9]\d*', Head)[0]), int(re.findall('[0-9]\d*', Head)[1])
##                    for i in range(D1, D2+1):
##                        Copy.pop(i - 1 + num)
##                        num -= 1
##            elif 'a' in x:
##                Head = x[0: x.index('a')]
##                List = x[x.index('a') + 1:]
##                if List.isdigit():
##                    Copy.insert(int(Head)+num, self.text2[int(List)-1])
##                    num += 1
##                else:
##                    D1, D2 = int(re.findall('[0-9]\d*', List)[0]), int(re.findall('[0-9]\d*', List)[1])
##                    for i in range(D1, D2+1):
##                        Copy.insert(int(Head) + num, self.text2[i - 1])
##                        num += 1
##        return Copy




        
