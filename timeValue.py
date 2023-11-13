# DICTIONARY
# N = Number of compounding periods
# I/Y = Interest rate per compounding period
# PV = Present value
# FV = Future value
# PMT = Annuity payments, or constant periodic cash flow

# EFFECTIVE ANNUAL RATE (EAR) / EFFECTIVE ANNUAL YIELD (EAY)
# EAR/EAY is the annual rate of return earned after adjustments are made for different compounding periods
# EAR = (1 + periodic rate) ** (total number of periods) - 1
# periodic rate = (stated annual rate) / (number of compounding periods per year)
# https://www.investopedia.com/terms/e/effectiveinterest.asp
def effectiveAnnualRate(ar, cp, years, *pr):
    if pr:
        ear = (1 + pr) ** (cp * years) - 1
    else:
        ear = (1 + (ar / cp)) ** (cp * years) - 1
    print("Effective annual rate: {}.".format(round(float(ear), 2)))
    return(round(float(ear), 2))

# FUTURE VALUE (FV) / COMPOUND VALUE
# FV is the amount to which a current deposit will grow over time when it is placed in an account paying compound interest
# FV = PV(1 + i/y) ** n
# Future value factor (or future value interest factor) = (1 + i/y) ** n
def futureValue(pv, iy, n):
    fv = pv * (1 + iy) ** n
    print("Future value: {}.".format(fv))
    return(round(float(fv), 2))

# PRESENT VALUE (PV) / DISCOUNT RATE / OPPORTUNTIY COST / REQUIRED RATE OF RETURN / COST OF CAPITAL
# PV is the amount that must be invested today, at a given rate of return over a given period of time, to end up with a specific future amount
# Present value factor (or present value interest factor or discount factor) = 1 / (1 + i/y) ** n
def presentValue(fv, iy, n):
    pv = fv / ((1 + iy) ** n)
    print("Present value: {}.".format(pv))
    return(round(float(pv), 2))

# https://www.investopedia.com/retirement/calculating-present-and-future-value-of-annuities/
def futureValueAnnuity(c, i, n, *d):
    if d:
        fva = c * (((((1 + i) ** n) - 1) / i) * (1 + i))
        print("Future value annuity (due): {}.".format(fva))
    else:
        fva = c * ((((1 + i) ** n) - 1) / i)
        print("Future value annuity (ordinary): {}.".format(fva))

    return(round(float(fva), 2))

def presentValueAnnuity(c, i, n, *d):
    if d:
        pva = c * ((((1 - (1 + i) ** -n)) / i) * (1 + i))
        print("Present value annuity (due): {}.".format(pva))
    else:
        pva = c * (((1 - (1 + i) ** -n)) / i)
        print("Present value annuity (ordinary): {}.".format(pva))

    return(round(float(pva), 2))

def presentValuePerpetuity(pmt, iy):
    pvp = pmt/iy
    print("Present value perpetuity: {}.".format(pvp))
    return(round(float(pvp), 2))


# RUN
# (1) annual rate, (2) compounding periods, (3) years, (4) periodic rate
#effectiveAnnualRate(ar, cp, years, pr)

# (1) present value, (2) rate of return per compounding period, (3) total number of compounding periods
#futureValue(pv, iy, n)

# (1) future value, (2) rate of return per compounding period, (3) total number of compounding periods
#presentValue(fv, iy, n)

#futureValueAnnuity(c, i, n)
#futureValueAnnuity(1000, .05, 5, 'due')

#presentValueAnnuity(c, i, n)
#presentValueAnnuity(1000, .05, 5, 'abc')

#presentValuePerpetuity(pmt, iy)
#presentValuePerpetuity(4.50, 0.08)