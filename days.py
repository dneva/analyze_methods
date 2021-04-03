from analysis import september,october,november,december
import matplotlib.pyplot as plt

for i in range(1,32):
    day=september.loc[(september['Data'] == f'9/{i}/2016')]
    print(day)
    if not day.empty:
        plt.plot(day['UNIXTime'],day['λ'],c='orange')
        plt.savefig(f'september/day{i}')
        plt.close()
for i in range(1,32):
    day=october.loc[(october['Data'] == f'10/{i}/2016')]
    if not day.empty:
        plt.plot(day['UNIXTime'],day['λ'],c='red')
        plt.savefig(f'october/day{i}')
        plt.close()
for i in range(1,32):
    day=november.loc[(november['Data'] == f'11/{i}/2016')]
    if not day.empty:
        plt.plot(day['UNIXTime'],day['λ'],c='violet')
        plt.savefig(f'november/day{i}')
        plt.close()
for i in range(1,32):
    day=december.loc[(december['Data'] == f'12/{i}/2016')]
    if not day.empty:
        plt.plot(day['UNIXTime'],day['λ'],c='blue')
        plt.savefig(f'december/day{i}')
        plt.close()
        
