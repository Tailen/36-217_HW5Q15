from numpy.random import binomial



def factorial(n):
    result = 1
    for i in range(1, (n+1)):
        result *= i
    return result

def choose(n, k):
    return (factorial(n) / factorial(k) / factorial(n-k))

def evaluate(x):
    E_P_given_x = 0
    for d in range(11):
        E_P_given_x += choose(10, d) * (150*min(x,d))
    return E_P_given_x * (0.5**10) - 75*x

def argmax():
    max_value = 0
    arg_max = 0
    for x in range(0, 15):
        E_P_given_x = evaluate(x)
        print('Expect profit if by', x, 'tickets:', E_P_given_x)
        if (E_P_given_x > max_value):
            max_value = E_P_given_x
            arg_max = x
    print('Should buy', arg_max, 'tickets')

argmax()



def simulated_profit(num_simulations, tickets_bought):
    profit_sum = 0
    for _ in range(num_simulations):
        demand = binomial(10, 0.5)
        profit = tickets_bought * (-75) + min(tickets_bought, demand) * 150
        profit_sum += profit
    return (profit_sum/num_simulations)

def MC_Q15(num_simulations):
    max_profit = 0
    arg_max = 0
    for i in range(0, 11):
        profit = simulated_profit(num_simulations, i)
        print('Simulated profit if by', i, 'tickets:', profit)
        if (profit > max_profit):
            max_profit = profit
            arg_max = i
    print('Should buy', arg_max, 'tickets')

MC_Q15(100000)