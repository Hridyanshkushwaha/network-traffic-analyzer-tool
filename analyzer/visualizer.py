import matplotlib.pyplot as plt


def plot_protocol_distribution(protocol_dist):
    plt.figure()
    plt.bar(protocol_dist.keys(), protocol_dist.values())
    plt.xlabel("Protocol Number")
    plt.ylabel("Packet Count")
    plt.title("Protocol Distribution")
    plt.show()
