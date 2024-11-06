def solution(brown, yellow):
    total = brown + yellow
    # col, row 최소 3
    for row in range(3, total):
        if total % row == 0:
            col = total // row
            if (col-2) * (row-2) == yellow:
                return col, row
            
            