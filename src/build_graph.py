import matplotlib.pyplot as plt
def make_graph(num, steps, bigIn, big):
    plt.plot(range(len(steps)), steps, linestyle='-', linewidth=1)
    plt.xlabel('Step\'s number')
    plt.ylabel('Value of a step')
    plt.title('{} steps for {} to reach 1'.format(len(steps), num))
    plt.annotate('Highest step\n ({}, {})'.format(bigIn, big),
                 xy=(bigIn, big),
                 xytext=(bigIn+(len(steps)/20), big-(big/20)),
                 arrowprops=dict(arrowstyle='->'),
    )
    plt.savefig('Graph{}.png'.format(num), dpi=500, format='png')
    plt.savefig('Graph{}.svg'.format(num), dpi=500, format='svg')
    plt.clf()
