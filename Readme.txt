Abdullah Al Mamun and Gabriel Morales
CSC 242
Project 3
April 15th, 2016

Files
*********************************
main.py
bayesian_network.py
exact_inference.py
rejection_sampling.py
likelyhood_sampling.py


Run Instructions
**********************************

<algorithm>: exact, rejection, likelihood, gibbs
<filename>: [For MAC] 		=> unix-linux/<filename>
			[For Windows] 	=> windows/<filename> 

For Exact Inference
~~~~~~~~~~~~~~~~~~~~~~~~~

	For MAC/Linux/Unix
	-------------------
	python main.py -<algorithm> <filename> <query>
	python main.py -<algorithm> <filename> <query> <given> <value>

	For Windows
	-------------------

For other algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~

	For MAC/Linux/Unix
	------------------- 
	python main.py -<algorithm> <filename> <SampleNumber> <query>
	python main.py -<algorithm> <filename> <SampleNumber> <query> <given> <value>

	For Windows
	-------------------

EXAMPLE RUN
^^^^^^^^^^^^^^^^^^^^^^^
.XML Files:
```````````
python main.py -exact unix-linux/aima-alarm.xml B J true M true
python main.py -exact unix-linux/aima-alarm.xml A E true
python main.py -rejection unix-linux/aima-alarm.xml 1000 B J true M True
python main.py -rejection unix-linux/aima-alarm.xml 1000 M A true


.BIF Files:
```````````
@@@@@@@@@@@@@@@@@@@@@@@@@@@ IMPORTANT THING TO KNOW @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
------------------------------------------------------------------------------------
<<<<<<<<<<<<<<<<<        FOR .BIF FILES, THERE ARE A LOT OF VARIABLES. TO SEE THE RESULTS SPECIALLY FOR EXACT INFERENCE YOU WILL HAVE TO GIVE A LOT OF EVIDENCE(GIVEN) VARIABLES. FOR alarm.bif FILE, THERE ARE 37 VARIABLES IN TOTAL. TO SEE THE RESULT REAL QUICK THERE HAS TO BE AT LEAST 26 VARIABLES AND THAT WILL TAKE APPROXIMATELY 13 SECONDS. FEWER THAN THAT WILL TAKE MORE TIME, IT WILL SEEM LIKE THE PROGRAM IS STUCK, BUT IT'S JUST STILL CALCULATING STUFF     >>>>>>>>>>>>>>>

python main.py -exact unix-linux/alarm.bif LVEDVOLUME HYPOVOLEMIA FALSE LVFAILURE FALSE HISTORY TRUE CVP LOW PCWP HIGH STROKEVOLUME NORMAL ERRLOWOUTPUT TRUE HRBP LOW HREKG HIGH ERRCAUTER FALSE HRSAT HIGH INSUFFANESTH TRUE ANAPHYLAXIS FALSE TPR LOW EXPCO2 ZERO KINKEDTUBE TRUE MINVOL ZERO FIO2 NORMAL PVSAT NORMAL SAO2 LOW PAP LOW PULMEMBOLUS TRUE SHUNT NORMAL INTUBATION ONESIDED PRESS HIGH DISCONNECT TRUE MINVOLSET LOW VENTMACH ZERO VENTTUBE ZERO VENTLUNG NORMAL


