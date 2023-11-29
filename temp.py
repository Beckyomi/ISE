weight = float(input("Enther your puppuy's weight in lbs followed by enter: "))
print(weight)

import cvxpy as cp
import math

x = cp.Variable(10, nonneg=True)
y = cp.Variable(10, boolean=True)

constraints = []

#Meet Protein Requirement
constraints.append(0.22*x[0]+0.21*x[1]+0.20*x[2]+0.19*x[3]+0.25*x[4]+0.25*x[5]
                   +0.32*x[6]+0.26*x[7]+0.24*x[8]+0.32*x[9]>=0.00220462*weight)

#Meet Fat Requirement
constraints.append(14*x[0]+11*x[1]+13*x[2]+17*x[3]+15*x[4]+14*x[5]+18*x[6]+16*
                   x[7]+14*x[8]+18*x[9]>=10*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
                    +x[7]+x[8]+x[9]))
constraints.append(14*x[0]+11*x[1]+13*x[2]+17*x[3]+15*x[4]+14*x[5]+18*x[6]+16*
                   x[7]+14*x[8]+18*x[9]<=16*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
                   +x[7]+x[8]+x[9]))

#Meet Fiber Requiremen
constraints.append(3.5*x[0]+4*x[1]+4*x[2]+3*x[3]+6*x[4]+4*x[5]+4*x[6]+3*x[7]+
                   5*x[8]+4*x[9]>=3.5*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]
                   +x[8]+x[9]))
constraints.append(3.5*x[0]+4*x[1]+4*x[2]+3*x[3]+6*x[4]+4*x[5]+4*x[6]+3*x[7]+
                   5*x[8]+4*x[9]<=4.5*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]
                  +x[8]+x[9]))

#Meet Phosphorus Requiremen
constraints.append(6.8*x[1]+x[4]+0.8*x[7]+0.7*x[8]>=0.6)
constraints.append(6.8*x[1]+x[4]+0.8*x[7]+0.7*x[8]<=1.3)

#Meet Vitamin E Requiremen
constraints.append(60/2.2*x[0]+100/2.2*x[1]+400/2.2*x[2]+100/2.2*x[4]+60/2.2*
                   x[5]+150/2.2*x[6]+250/2.2*x[7]+150/2.2*x[9]>=weight)
constraints.append(60/2.2*x[0]+100/2.2*x[1]+400/2.2*x[2]+100/2.2*x[4]+60/2.2*x[5]+150/2.2*x[6]
                   +250/2.2*x[7]+150/2.2*x[9]<=weight*2)

#Meet Omega_6 Requiremen
constraints.append(2.2*x[0]+2*x[1]+2.5*x[2]+0*x[3]+2.91*x[4]+2.05*x[5]+2.80*x[6]+1.6*x[7]+3*x[8]
                   +3.1*x[9]>=2*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]))
constraints.append(2.2*x[0]+2*x[1]+2.5*x[2]+0*x[3]+2.91*x[4]+2.05*x[5]+2.80*x[6]+1.6*x[7]+3*x[8]
                   +3.1*x[9]<=2.9*(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]))

#Meet CALORI Requiremen
constraints.append(3631/2.2*x[0]+3454/2.2*x[1]+4334/2.2*x[2]+3855/2.2*x[3]+3476/2.2*x[4]+3646/2.2
                   *x[5]+3719/2.2*x[6]+4004/2.2*x[7]+3618/2.2*x[8]+3719/2.2*x[9]>=90*math.sqrt(
                       (math.sqrt((weight/2.2)*(weight/2.2)*(weight/2.2)))))


constraints.append(x[0]<=y[0]*weight*0.03)
constraints.append(x[1]<=y[1]*weight*0.03)
constraints.append(x[2]<=y[2]*weight*0.03)
constraints.append(x[3]<=y[3]*weight*0.03)
constraints.append(x[4]<=y[4]*weight*0.03)
constraints.append(x[5]<=y[5]*weight*0.03)
constraints.append(x[6]<=y[6]*weight*0.03)
constraints.append(x[7]<=y[7]*weight*0.03)
constraints.append(x[8]<=y[8]*weight*0.03)
constraints.append(x[9]<=y[9]*weight*0.03)

constraints.append(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]>=weight*0.03)
constraints.append(y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7]+y[8]+y[9]<=3)
    

obj_func = 1.52*x[0]+2.84*x[1]+2.43*x[2]+7.41*x[3]+1.83*x[4]+2.32*x[5]+2.11*x[6]+1.43*x[7]+2.17*x[8]+2.11*x[9]


problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print("y =")
print(y.value)
