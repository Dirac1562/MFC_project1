## OPTIMIZATION LP Problem:
import pulp
import pandas

def get_file(file_name):
    with open("files\\" + file_name + ".txt") as file: # opening the file with the problem
        lst = []
        for lines in file.readlines():
            lst.append(lines)
        return lst

objective_f = pulp.LpProblem("KASMO Industry Limited (KIL)", pulp.LpMaximize)

#decision variable

X1 = pulp.LpVariable("1 tablet per pack", 0, None, pulp.LpInteger)
X2 = pulp.LpVariable("3 tablets per pack", 0, None, pulp.LpInteger)
X3 = pulp.LpVariable("12 tablets per pack", 0, None, pulp.LpInteger)
X4 = pulp.LpVariable("24 tablets per pack", 0, None, pulp.LpInteger)

objective_f += 14.36 * X1 + 33.08 * X2 + 112.32 * X3 + 1023.20 * X4,  "Total profit"

objective_f += 0.88995 * X1 + 2.66984 * X2 + 10.67937 * X3 + 106.793650 * X4 <= 16820, "Caustic Soda"
objective_f += 2.14815 * X1 + 6.44444 * X2 + 25.77778 * X3 + 257.77778 * X4 <= 40600, "Palm Kernel Oil"
objective_f += 0.00153 * X1 + 0.00460 * X2 + 0.01841 * X3 + 0.18413 * X4 <= 29, "Colourant"
objective_f += 0.00614 * X1 + 0.01841 * X2 + 0.07365 * X3 + 0.73651 * X4 <= 116, "Perfume"
objective_f += 0.02762 * X1 + 0.08286 * X2 + 0.33143 * X3 + 3.31429 * X4 <= 522, "Disinfectant"

objective_f.solve()

#print(pulp.LpStatus[objective_f.status])
solution = [{name : name.value()} for name in objective_f.variables()]
# for value in objective_f.variables():
#     print("The number of {} we have to sold is : {} ".format(value, value.value()))
print(pandas.DataFrame(solution))
sr = [{"Constraint Name" : cname, "Slack Variable" : cinfo.slack , "Shadow price" : cinfo.pi} for cname, cinfo in objective_f.constraints.items()]
print(pandas.DataFrame(sr))


#files
