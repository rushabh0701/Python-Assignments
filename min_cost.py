from pulp import *

LP_minimize_cost = pulp.LpProblem("Minimize Cost",pulp.LpMinimize)

Fuel_cost_leg1 = 4.15
Fuel_cost_leg2 = 4.25
Fuel_cost_leg3 = 4.10
Fuel_cost_leg4 = 4.18

Min_fuel_leg1 = 24000
Max_fuel_leg1 = 35000
Reg_fuel_consume_leg1= 12000

Min_fuel_leg2 = 15000 
Max_fuel_leg2 = 23000 
Reg_fuel_consume_leg2 = 7000

Min_fuel_leg3 = 9000
Max_fuel_leg3 = 17000
Reg_fuel_consume_leg3 = 3000

Min_fuel_leg4 = 11000
Max_fuel_leg4 = 20000
Reg_fuel_consume_leg4 = 5000


Fuel_refill_leg1 = pulp.LpVariable('Fuel_refill_leg1', lowBound=0, cat='Continuous')
Fuel_refill_leg2 = pulp.LpVariable('Fuel_refill_leg2', lowBound=0, cat='Continuous')
Fuel_refill_leg3 = pulp.LpVariable('Fuel_refill_leg3', lowBound=0, cat='Continuous')
Fuel_refill_leg4 = pulp.LpVariable('Fuel_refill_leg4', lowBound=0, cat='Continuous')

Fuel_left_leg1 = pulp.LpVariable('Fuel_left_leg1', lowBound=0, cat='Continuous')
Fuel_left_leg2 = pulp.LpVariable('Fuel_left_leg2', lowBound=0, cat='Continuous')
Fuel_left_leg3 = pulp.LpVariable('Fuel_left_leg3', lowBound=0, cat='Continuous')
Fuel_left_leg4 = pulp.LpVariable('Fuel_left_leg4', lowBound=0, cat='Continuous')

Fuel_carried_leg1 = pulp.LpVariable('Fuel_carried_leg1', cat='Continuous')
Fuel_carried_leg2 = pulp.LpVariable('Fuel_carried_leg2', cat='Continuous')
Fuel_carried_leg3 = pulp.LpVariable('Fuel_carried_leg3', cat='Continuous')
Fuel_carried_leg4 = pulp.LpVariable('Fuel_carried_leg4', cat='Continuous')

Fuel_consume_leg1 = pulp.LpVariable('Fuel_consume_leg1', lowBound=Reg_fuel_consume_leg1, cat='Continuous')
Fuel_consume_leg2 = pulp.LpVariable('Fuel_consume_leg2', lowBound=Reg_fuel_consume_leg2, cat='Continuous')
Fuel_consume_leg3 = pulp.LpVariable('Fuel_consume_leg3', lowBound=Reg_fuel_consume_leg3, cat='Continuous')
Fuel_consume_leg4 = pulp.LpVariable('Fuel_consume_leg4', lowBound=Reg_fuel_consume_leg4, cat='Continuous')

Fuel_consume_leg1 = Reg_fuel_consume_leg1 + 50*((Fuel_carried_leg1-Min_fuel_leg1)/1000)
Fuel_consume_leg2 = Reg_fuel_consume_leg2 + 50*((Fuel_carried_leg2-Min_fuel_leg2)/1000)
Fuel_consume_leg3 = Reg_fuel_consume_leg3 + 50*((Fuel_carried_leg3-Min_fuel_leg3)/1000)
Fuel_consume_leg4 = Reg_fuel_consume_leg4 + 50*((Fuel_carried_leg4-Min_fuel_leg4)/1000)

Fuel_left_leg1 = Fuel_carried_leg1 - Fuel_consume_leg1
Fuel_left_leg2 = Fuel_carried_leg2 - Fuel_consume_leg2
Fuel_left_leg3 = Fuel_carried_leg3 - Fuel_consume_leg3
Fuel_left_leg4 = Fuel_carried_leg4 - Fuel_consume_leg4

Fuel_refill_leg1 = Fuel_carried_leg1 - Fuel_left_leg4
Fuel_refill_leg2 = Fuel_carried_leg2 - Fuel_left_leg1
Fuel_refill_leg3 = Fuel_carried_leg3 - Fuel_left_leg2
Fuel_refill_leg4 = Fuel_carried_leg4 - Fuel_left_leg3

#Fuel_carried_leg1 = Fuel_refill_leg1 + Fuel_left_leg4
#Fuel_carried_leg2 = Fuel_refill_leg2 + Fuel_left_leg1
#Fuel_carried_leg3 = Fuel_refill_leg3 + Fuel_left_leg2
#Fuel_carried_leg4 = Fuel_refill_leg4 + Fuel_left_leg3

#Constraints

LP_minimize_cost += Fuel_carried_leg1 <= 36000
LP_minimize_cost += Fuel_carried_leg1 >= 24000
LP_minimize_cost += Fuel_carried_leg2 <= 23000
LP_minimize_cost += Fuel_carried_leg2 >= 15000
LP_minimize_cost += Fuel_carried_leg3 <= 17000
LP_minimize_cost += Fuel_carried_leg3 >= 9000
LP_minimize_cost += Fuel_carried_leg4 <= 20000
LP_minimize_cost += Fuel_carried_leg4 >= 11000


### objective function 

LP_minimize_cost += (Fuel_cost_leg1)*(Fuel_refill_leg1) + (Fuel_cost_leg2)*(Fuel_refill_leg2) + (Fuel_cost_leg3)*(Fuel_refill_leg3) + (Fuel_cost_leg4)*(Fuel_refill_leg4), "minimize_cost"

LP_minimize_cost.solve()

print(pulp.LpStatus[LP_minimize_cost.status])

print("==================================================================================================================================================================================")
print("Leg                     Minimum Fuel Required          Maximum Fuel Allowed          Regular Fuel Consumption          Fuel Price per gallon            Fuel Refilled at each leg")
print("==================================================================================================================================================================================")
print("Atlanta-Los Angeles    ",    Min_fuel_leg1,"                        ",Max_fuel_leg1,"                       ",Reg_fuel_consume_leg1,"                           ",Fuel_cost_leg1,"                           ",value(Fuel_refill_leg1))
print("Los Angeles-Houston    ",    Min_fuel_leg2,"                        ",Max_fuel_leg2,"                       ",Reg_fuel_consume_leg2,"                            ",Fuel_cost_leg2,"                           ",value(Fuel_refill_leg2))
print("Houston-New Orleans    ",    Min_fuel_leg3,"                         ",Max_fuel_leg3,"                       ",Reg_fuel_consume_leg3,"                            ",Fuel_cost_leg3,"                            ",value(Fuel_refill_leg3))
print("New Orleans-Atlanta    ",    Min_fuel_leg4,"                        ",Max_fuel_leg4,"                       ",Reg_fuel_consume_leg4,"                            ",Fuel_cost_leg4,"                           ",value(Fuel_refill_leg4))
print("\n")
print ("Total Cost: $",value(LP_minimize_cost.objective))
