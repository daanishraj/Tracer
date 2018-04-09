###########################################################################
#                            Set Constants                                #
###########################################################################
START_AGE = 22            #
END_AGE = 100             #
RETIRE_AGE = 65           # retirement age
N_W = 1001
LOWER_BOUND_W = 1         # lower bound of wealth
UPPER_BOUND_W = 15000000    # upper bound of wealth
EXPAND_FAC = 3
N_C = 3001
LOWER_BOUND_C = 0
GAMMA = 4                 # risk preference parameter
R = 0.02                  # risk-free rate
DELTA = 0.99              # discount factor
MU = 0                    # expectation of income shocks
N_SIM = 100000            # number of draws
INIT_WEALTH = 0

AltDeg = 4
flag = 'ppt'  #, 'orig' 'rho'  # 'ppt'
run_dp = True
N = 1

education_level = {
    1: 'No High School',
    2: 'High School Graduates',
    4: 'College Graduates'
}

# replacement rate of retirement earnings (lambda)
ret_frac = {
    1: 0.6005,
    2: 0.5788,
    4: 0.4516,
}

# replacement rate of unemployment earnings (theta)
unemp_frac = {
    1: 0.7891,
    2: 0.7017,
    4: 0.5260 # 1-10**(-5),  # 0.5260,
}

# probability of suffering an unemployed spell (pi)
unempl_rate = {
    1: 0.2024,
    2: 0.1438,
    4: 0.0738 # 10**(-5),  # 0.0738,
}

# rho
# rho = 0.900796641891997
rho = 0.931001221
TERM = 10

# ppt
ppt = 10031.76 # 3483.25

####################################################
N_D = 1001
UPPER_BOUND_D = 25000
N_P = 2001

I = 0.07
