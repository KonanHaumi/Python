import math


def volume(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """Правило трапеций
               rtol - желаемая относительная точность вычислений
               nseg0 - начальное число отрезков разбиения"""
            rtol = 1e-8
            nseg0 = 1
            nseg = nseg0
            old_ans = 0.0
            dx = 1.0 * (b - a) / nseg
            ans = 0.5 * (func(a) + func(b))
            for i in range(1, nseg):
                ans += func(a + i * dx)
            ans *= dx
            err_est = max(1, abs(ans))
            while (err_est > abs(rtol * ans)):
                old_ans = ans

                def _rectangle_rule(func, a, b, nseg, frac):
                    """Обобщённое правило прямоугольников."""
                    dx = 1.0 * (b - a) / nseg
                    sum = 0.0
                    xstart = a + frac * dx  # 0 <= frac <= 1 задаёт долю смещения точки,
                    # в которой вычисляется функция,
                    # от левого края отрезка dx
                    for i in range(nseg):
                        sum += func(xstart + i * dx)

                    return sum * dx

                def midpoint_rectangle_rule(func, a, b, nseg):
                    """Правило прямоугольников со средней точкой"""
                    return _rectangle_rule(func, a, b, nseg, 0.5)

                ans = 0.5 * (ans + midpoint_rectangle_rule(func, a, b, nseg))  # новые точки для уточнения интеграла
                # добавляются ровно в середины предыдущих отрезков
                nseg *= 2
                err_est = abs(ans - old_ans)
            return ans * math.pi
        return wrapper
    return decorator


@volume(a = 1, b = 5)  # границы фигуры
def f2(x):
    func = x**2  # желаемая функция 
    return func ** 2


# вывод
print(f2())
