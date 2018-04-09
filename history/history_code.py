# # cal_ce, to test if consumption is negative
# if any(c < 0):
#     print(w[c < 0])
#     print(age)
#     print(c[c < 0])
#
#     w_test = np.linspace(1, 4000, num=1000)
#     plt.plot(c_df.loc[:3, str(END_AGE)], c_df.loc[:3, str(age)], 'o', w_test, spline(w_test), '-')
#     plt.xlabel('Wealth')
#     plt.ylabel('Consumption')
#     # plt.show()
#     plt.savefig('negative_consumption_1.png')
#
#     spline.c[:2, 0] = 0
#     spline.c[2, 0] = (c_df.loc[1, str(age)] - c_df.loc[0, str(age)]) / (
#             c_df.loc[1, str(END_AGE)] - c_df.loc[0, str(END_AGE)])
#     plt.figure()
#     plt.plot(c_df.loc[:3, str(END_AGE)], c_df.loc[:3, str(age)], 'o', w_test, spline(w_test), '-')
#     plt.xlabel('Wealth')
#     plt.ylabel('Consumption')
#     # plt.show()
#     plt.savefig('negative_consumption_2.png')
#     sys.exit('negative consumption!')



# # income - deterministic component
# ret_income_vec = income_ret * np.ones(END_AGE - RETIRE_AGE)  # TODO: wrong here, add perm shock at last working period to retirement income
# income = np.append(income_bf_ret, ret_income_vec)
#
# # income - add income shocks
# rn_perm = np.random.normal(MU, sigma_perm_shock, (N_SIM, RETIRE_AGE - START_AGE + 1))
# rand_walk = np.cumsum(rn_perm, axis=1)
# rn_tran = np.random.normal(MU, sigma_tran_shock, (N_SIM, RETIRE_AGE - START_AGE + 1))
#
# zeros = np.zeros((N_SIM, END_AGE - RETIRE_AGE))
# perm = np.append(rand_walk, zeros, axis=1)
# tran = np.append(rn_tran, zeros, axis=1)
#
# inc_with_inc_risk = np.multiply(np.exp(perm) * np.exp(tran), income)  # inc.shape: (simu_N x 79)




# # CE output
# ce_fp = os.path.join(base_path, 'results', 'ce.xlsx')
#
# col_names = ['Consumption CE', 'Total Wealth CE']
# idx_names = education_level.values()
# ce = pd.DataFrame(index=idx_names, columns=col_names)
# for AltDeg in [4]:
#     ce.loc[education_level[AltDeg]] = cal_certainty_equi(age_coeff, std, surv_prob, AltDeg)
#
# print(ce)
# ce.to_excel(ce_fp)



# # inner for-loop
# for i in range(N_W):
#
#     consmp = np.linspace(0, grid_w[i], N_C)
#     u_r = utility(consmp, GAMMA)
#     u_r = u_r[None].T
#
#     savings = grid_w[i] - np.linspace(0, grid_w[i], N_C)
#     savings_incr = savings * (1 + R)
#     savings_incr = savings_incr[None].T
#
#     if t + START_AGE >= RETIRE_AGE:
#         expected_value = exp_val_r(income_ret, np.exp(inc_shk_perm(RETIRE_AGE - START_AGE + 1)), savings_incr, grid_w,
#                                    v[0, :], weights)
#     else:
#         expected_value = exp_val(income_with_tran[:, t + 1], np.exp(inc_shk_perm(t + 1)),
#                                  savings_incr, grid_w, v[0, :], weights, t + START_AGE, flag)  # using Y_t+1 !
#
#     v_array = u_r + DELTA * prob[t] * expected_value  # v_array has size N_C-by-1
#     v[1, i] = np.max(v_array)
#     pos = np.argmax(v_array)
#     c[1, i] = consmp[pos]
#
# # dump consumption array and value function array
# c_collection[str(t + START_AGE)] = c[1, :]
# v_collection[str(t + START_AGE)] = v[1, :]
#
# # change v & c for calculation next stage
# v[0, :] = v[1, :]
# c[0, :] = c[1, :]  # useless here