# import sys
import os
import net_prof
target_host = "x4102c5s5b0n0.hostmgmt2102.cm.aurora.alcf.anl.gov"
net_prof.collect("/sys/class/cxi/","/lus/flare/projects/datascience/kaushik/network/net-prof-tests/ping-test/before.json")
os.system(f"ping -c 4 {target_host}") 
net_prof.collect("/sys/class/cxi/","/lus/flare/projects/datascience/kaushik/network/net-prof-tests/ping-test/after.json")
summary = net_prof.summarize("/lus/flare/projects/datascience/kaushik/network/net-prof-tests/ping-test/before.json", "/lus/flare/projects/datascience/kaushik/network/net-prof-tests/ping-test/after.json")
net_prof.dump(summary)
net_prof.dump_html(summary, "/lus/flare/projects/datascience/kaushik/network/net-prof-tests/ping-test/net_prof_report.html")
