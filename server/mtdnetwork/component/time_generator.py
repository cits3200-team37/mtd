from scipy.stats import expon
from scipy.stats import norm
from scipy.stats import uniform
from scipy.stats import weibull_min
from scipy.stats import poisson


def exponential_variates(loc, scale):
    return expon.rvs(loc=loc, scale=scale, size=1)[0]


def normal_variates(loc, scale):
    return norm.rvs(loc=loc, scale=scale, size=1)[0]


def uniform_variates(loc, scale):
    return uniform.rvs(loc=loc, scale=scale, size=1)[0]


def weibull_variates(loc, scale):
    return weibull_min.rvs(loc=loc, scale=scale, size=1)[0]


def poisson_variates(loc, scale):
    return poisson.rvs(loc=loc, scale=scale, size=1)[0]
