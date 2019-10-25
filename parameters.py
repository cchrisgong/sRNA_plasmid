# integration parameters:

N = 4000000
h = 4e-4

#scanning resolutions (increments) for 10 parameters

parnames = ["g", "pm", "bm", "ps", "bs", "hplus", "hminus", "bc", "pp", "bp"]
partitles = ["gene copy", "production rate of mRNA", "degradation rate of mRNA", "production rate of sRNA", "degradation rate of sRNA", "binding rate of the mRNA-sRNA complex", "unbinding rate of complex", "degration rate of complex", "production rate of toxic protein", "degradation rate of toxic protein"]

#parlist   =     [g,    pm, 	bm, 	ps, 	bs, 	hpl,	hmi,  	bc,  	pp, 	bp]
resolution =     [1e0 , 5e-1, 	3e-2,	5e-1, 	5e-1, 	1e-2 , 	5e-2, 	1e-2, 	1e0 , 	5e-3]

#defaultvalue =  [8. , 4., .4,10., 1., 10., .2,  .1, 20., .5]

#scanning starting points
range_startlist= [7e0, 	1e-2, 	1e-2, 	1e-2, 1e-1, 	1e-2, 	1e-2, 	6e-1, 	1e-2, 	0.065e0]
#scanning ending points
range_endlist =  [8e0,	12e0, 	2.5e0, 	20e0, 	5e0, 	2e0, 	10e0, 	1.6e0, 	5e0, 	1.1e0]

# default system parameter values (total of 10):

g = 6e0 # gene copy number/ plasmid copy number

pm = 1e0 # "p"roduction rate of mRNA
bm = 2e-1 # degradation ("b"reakdown) rate of mRNA

ps = 6e0 # "p"roduction rate of sRNA
bs = 1e0 # degradation ("b"reakdown) rate of sRNA

hplus = 20e0 # binding rate of the mRNA-sRNA complex
hminus = 1e0 # unbinding rate of complex, * * * 0 if the binding is perfect/irreversible * * *

#hplus = 20e0 # binding rate of the mRNA-sRNA complex
#hminus = 1e0 # unbinding rate of complex, * * * 0 if the binding is perfect/irreversible * * *
bc = 2e-1 # degration ("b"reakdown) rate of complex

pp = 5e0 # "p"roduction rate of toxic protein
bp = 3.5e-2 # degradation ("b"reakdown) rate of protein
