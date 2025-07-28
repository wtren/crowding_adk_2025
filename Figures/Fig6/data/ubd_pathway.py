import os 
import sys
import argparse

parser = argparse.ArgumentParser(description='Extract chemical states from ts file')
parser.add_argument('-i', type=str, help='input file: xxxx.ts')
parser.add_argument('-o', type=str, help='output file: xxxx.csv')
args = parser.parse_args()

def cata_pathway(outfile, traj, steps, init='DD'):
    nf = len(traj)
    if('DD' not in traj):
        sys.exit("Error! No DD state in this trajectory!")
    else:
        cont = []
        i0 = traj.index('DD')
        while(i0 < nf):
            if('DD' not in traj[i0+1:]):
                with open(outfile, "w") as fp:
                    for line in cont:
                        fp.write("%s\n" % line)
                sys.exit("Caution! No cycle in this trajectory!")
            else:
                i1 = traj[i0+1:].index('DD')
                # print(i0, i1, traj[i0], traj[i0+i1+1])
                rpath = ['DD']
                ind = [i0]
                ind2 = [str(steps[i0])]
                if(i1 > 0):
                    # rpath = ['DD']
                    # ind = [i0]
                    # ind2 = [steps[i0]]
                    j = i0+1
                    while(j<i0+1+i1):
                        ss_i = traj[j]
                        if(ss_i in traj[j+1:i0+i1+1]):
                            j2 = traj[i0+i1:j:-1].index(ss_i)
                            j = i0+i1 - j2
                        rpath.append(ss_i)
                        ind.append(j)
                        ind2.append( str(steps[j]) )
                        j = j + 1
                    # if(rpath != ['DD', 'TM']):
                        # print('-'.join(rpath), ind2)
                i0 = i0 + i1 + 1
                rpath.append('DD')
                ind.append(i0)
                ind2.append( str(steps[i0]) )
                if(rpath != ['DD', 'TM', 'DD'] and rpath != ['DD', 'DD'] and 'TM' in rpath):
                    line = '-'.join(rpath) + ' ' + ' '.join(ind2)
                    cont.append(line)
                    print(line)

if __name__ == "__main__":
    infile = args.i
    outfile = args.o
    print(infile)
    with open(infile, "r") as f1:
        cont = f1.readlines()
    ss_traj = []
    steps = []
    for line in cont:
        if(line[0] == '#'):
            continue
        else:
            tmp = line.split()
            ss_traj.append( tmp[4].strip() + tmp[5].strip() )
            steps.append(int(tmp[0]))
    # print(ss_traj)
    # print(steps)
    cata_pathway(outfile, ss_traj, steps)
