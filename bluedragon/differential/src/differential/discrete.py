def diff(t: list, x: list):
    """
    Calculate the discrete derivative of a time series

    variables:
    t: list, time value t_k, k is the index of time
    k: list, signal value x
    len(t) == len(k)
    """
    assert len(t) == len(x)

    v = [None]
    for k in range(1, len(t)):
        dt = t[k] - t[k-1]
        if dt == 0:
            raise ZeroDivisionError(f"Zero tiem difference at index {k}")
        v.append((x[k] - x[k-1]) / dt)

    return v


print(diff([1,2,3], [7,8,9]))
print(diff([1], [2,3]))
