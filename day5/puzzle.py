

def parse(lines):
    return lines


def solve(data):
    seat_ids = []

    for a in data:
        a.rstrip()
        rows = a[0:7]
        cols = a[7:]

        rows_lower = 0
        rows_upper = 127
        for row in rows:
            if row == 'B':
                rows_lower += (rows_upper - rows_lower) / 2
                rows_lower += 1

            elif row == 'F':
                rows_upper -= (rows_upper - rows_lower) / 2
                rows_upper -= 1

        cols_lower = 0
        cols_upper = 7
        for col in cols:
            if col == 'R':
                cols_lower += (cols_upper - cols_lower) / 2
                cols_lower += 1

            elif col == 'L':
                cols_upper -= (cols_upper - cols_lower) / 2
                cols_upper -= 1

        seat_id = (rows_lower * 8) + cols_lower
        seat_ids.append(seat_id)

    # myseat
    for seat in range(min(seat_ids), max(seat_ids)):
        if seat not in seat_ids:
            return seat

    # highest
    return max(seat_ids)
