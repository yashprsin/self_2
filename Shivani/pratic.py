wall_a = 87
wall_b = 121
wall_c = 25

new_wall_a = int(input("Enter new walls a: "))
new_wall_b = int(input("Enter new walls b: "))
new_wall_c = int(input("Enter new walls c: "))

wall_a_epx = 250000
wall_b_epx = 500000
wall_c_epx = 1000000

total_exp_of_wall_a = (wall_a * wall_a_epx)
total_exp_of_wall_b = (wall_b * wall_b_epx)
total_exp_of_wall_c = (wall_c * wall_c_epx)

complete_of_wall_a = wall_a + wall_b
complete_of_wall_a_epx = complete_of_wall_a * total_exp_of_wall_a

if new_wall_a < wall_a and new_wall_b < wall_b and new_wall_c < wall_c:
    your_epx = wall_a - new_wall_a and wall_b - new_wall_b and wall_c - new_wall_c
    print(your_epx)
elif new_wall_a > wall_a and new_wall_b > wall_b and new_wall_c > wall_c:
    your1_epx = new_wall_a - wall_a and new_wall_b - wall_b and new_wall_c - wall_c
    print(your1_epx)
