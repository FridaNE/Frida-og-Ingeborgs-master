#!/usr/bin/env python
# coding: utf-8

# In[9]:


# https://tutorials.sciml.ai/html/introduction/03-optimizing_diffeq_code.html
import math 
import numpy as np
from latexifier import latexify
import matplotlib.pyplot as plt
from scipy.integrate import odeint

π = 0.048                                               # equity premium 
σ = 0.1789                                              # volatility of equity return (std)
γ = 2.0                                               # risk aversion parameter
#const γ = 2.0
#const ξ = γ_1 - γ_2
g = 0.015
ρ = 0.04                                                # discount rate
r = 0.025                                               # risk-free rate 
h = 3.0                                                 # habit
θ = 0.00      # habit change of rate 
α=π/(γ*σ**2)

η=(1/γ)*ρ+(1-1/γ)*(r+(1/2)*(α*π))                            # calculate eta (c/A) upper bound 


t=10

ω=1/η

print (η)
print (ω)


# In[ ]:





# In[ ]:




