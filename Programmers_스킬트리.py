def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp =""
        for s in tree:
            if s in skill:
                tmp += s
        if skill[:len(tmp)]==tmp:
            answer +=1
    return answer