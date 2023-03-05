import json
from typing import Counter

with open("packets.json") as f:
    packets = json.load(f)

collected_packets: list[tuple[str, str]] = []
last_cwd = "0"
for packet in packets:
    layers = packet["_source"]["layers"]

    if "tcp" in layers:
        tcp = layers["tcp"]
        tcp_flags =tcp["tcp.flags_tree"]

        push = bool(int(tcp_flags["tcp.flags.push"]))
        ack = bool(int(tcp_flags["tcp.flags.ack"]))

        if push and ack and "ftp" in layers:
            cwd = layers["ftp.current-working-directory"]
            last_cwd = cwd
            # print(f"{cwd=}")

        if push and ack and "data" in layers:
            data = layers["data"]["data.data"]
            collected_packets.append((data, last_cwd))
            # print(f"{data=}")

print(Counter(i[1] for i in collected_packets))

for packet, cwd in sorted(collected_packets, key=lambda t: int(t[1])):
    value = int(packet, base=16)
    print(chr(value), end="")

