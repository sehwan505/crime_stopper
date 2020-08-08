from sklearn.ensemble import RandomForestClassifier
import read_csv

data = read_csv.count_list("2020-08-05",["자영","빅데이터","이","이란"])

rf = RandomForestClassifier(n_jobs=-1)
rf.fit(data,ans)
result = rf.predict(new_data)

