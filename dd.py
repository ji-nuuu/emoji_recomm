
for n in range(num_emojis):
  file_name = name_list[n][1:-1] + ".csv"
  df = pd.read_csv(file_name, encoding = 'utf-8')
  print(df)