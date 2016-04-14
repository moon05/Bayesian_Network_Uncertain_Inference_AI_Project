net Asia_dsl
{
 HEADER = 
  {
   ID = Asia_dsl;
   NAME = "Asia network by David Spiegelhalter";
   COMMENT = "This is an example graphical model useful in \ 
   demonstrating basics concepts of Bayesian networks in \ 
   diagnosis.\r\nIt first appeared in:\r\nLauritzen, Steffen L. & \ 
   Spiegelhalter, David J. (1988). Local computations with \ 
   probabilities on graphical structures and their application to \ 
   expert systems, Journal of the Royal Statistical Society B, \ 
   50(2):157-224.";
  };
 CREATION = 
  {
  };
 NUMSAMPLES = 1000;
 SCREEN = 
  {
   POSITION = 
    {
     CENTER_X = 0;
     CENTER_Y = 0;
     WIDTH = 76;
     HEIGHT = 36;
    };
   COLOR = 16250597;
   SELCOLOR = 12303291;
   FONT = 1;
   FONTCOLOR = 0;
   BORDERTHICKNESS = 3;
   BORDERCOLOR = 12255232;
  };
 WINDOWPOSITION = 
  {
   CENTER_X = 0;
   CENTER_Y = 0;
   WIDTH = 0;
   HEIGHT = 0;
  };
 BKCOLOR = 0;
 SCREENCOMMENT =  { (403, 132, 228, 220),"This is an example graphical \ 
 model useful in demonstrating basics concepts of Bayesian networks in \ 
 diagnosis.\r\nIt first appeared in:\r\nLauritzen, Steffen L. & \ 
 Spiegelhalter, David J. (1988). Local computations with probabilities \ 
 on graphical structures and their application to expert systems, \ 
 Journal of the Royal Statistical Society B, 50(2):157-224."};

 node VisitToAsia
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = VisitToAsia;
     NAME = "Visit To Asia?";
     COMMENT = "The node models whether the individual in question \ 
     visited Asia recently. This is considered to be a risk factor in \ 
     tuberculosis.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 55;
       CENTER_Y = 41;
       WIDTH = 80;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (NoVisit, Visit);
     PROBABILITIES = (0.99000000, 0.01000000);
    };
  };

 node Tuberculosis
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Tuberculosis;
     NAME = "Tuberculosis?";
     COMMENT = "Presence or absence of tuberculosis.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 55;
       CENTER_Y = 100;
       WIDTH = 78;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (VisitToAsia);
   DEFINITION = 
    {
     NAMESTATES = (Absent, Present);
     PROBABILITIES = (0.99000000, 0.01000000, 0.95000000, 0.05000000);
    };
  };

 node Smoking
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Smoking;
     NAME = "Smoking?";
     COMMENT = "Does the individual smoke or not? This is a serious \ 
     risk factor in both lung cancer and in bronchitis.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 205;
       CENTER_Y = 41;
       WIDTH = 67;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = ();
   DEFINITION = 
    {
     NAMESTATES = (NonSmoker, Smoker);
     PROBABILITIES = (0.50000000, 0.50000000);
    };
  };

 node LungCancer
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = LungCancer;
     NAME = "Lung Cancer?";
     COMMENT = "Does the individual suffer from lung cancer?";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 156;
       CENTER_Y = 100;
       WIDTH = 82;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (Smoking);
   DEFINITION = 
    {
     NAMESTATES = (Absent, Present);
     PROBABILITIES = (0.99000000, 0.01000000, 0.90000000, 0.10000000);
    };
  };

 node TbOrCa
  {
   TYPE = TRUTHTABLE;
   HEADER = 
    {
     ID = TbOrCa;
     NAME = "Tuberculosis or Lung Cancer?";
     COMMENT = "Does the individual suffer from either tuberculosis or \ 
     lung cancer? This node models practically existence of changes in \ 
     the lungs, such as presence of condensed mass in the lungs.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 104;
       CENTER_Y = 160;
       WIDTH = 75;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (Tuberculosis, LungCancer);
   DEFINITION = 
    {
     NAMESTATES = (Nothing, CancerORTuberculosis);
     RESULTINGSTATES = (Nothing, CancerORTuberculosis, 
     CancerORTuberculosis, CancerORTuberculosis);
    };
  };

 node XRay
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = XRay;
     NAME = "X-Ray Result";
     COMMENT = "This node models the X-ray result. Both tuberculosis \ 
     and lung cancer can be discovered on the X-ray because of presence \ 
     of condensed mass in the lungs.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 55;
       CENTER_Y = 221;
       WIDTH = 78;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (TbOrCa);
   DEFINITION = 
    {
     NAMESTATES = (Normal, Abnormal);
     PROBABILITIES = (0.95000000, 0.05000000, 0.02000000, 0.98000000);
    };
  };

 node Bronchitis
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Bronchitis;
     NAME = "Bronchitis?";
     COMMENT = "Does the individual suffer from bronchitis?";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 245;
       CENTER_Y = 100;
       WIDTH = 70;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (Smoking);
   DEFINITION = 
    {
     NAMESTATES = (Absent, Present);
     PROBABILITIES = (0.70000000, 0.30000000, 0.40000000, 0.60000000);
    };
  };

 node Dyspnea
  {
   TYPE = CPT;
   HEADER = 
    {
     ID = Dyspnea;
     NAME = "Dyspnea?";
     COMMENT = "Does the individual suffer from dyspnea (shortness of \ 
     breath)? Each of the diseases modeled can result in shortness of \ 
     breath.";
    };
   SCREEN = 
    {
     POSITION = 
      {
       CENTER_X = 156;
       CENTER_Y = 221;
       WIDTH = 76;
       HEIGHT = 36;
      };
     COLOR = 16250597;
     SELCOLOR = 12303291;
     FONT = 1;
     FONTCOLOR = 0;
     BORDERTHICKNESS = 1;
     BORDERCOLOR = 12255232;
    };
   PARENTS = (TbOrCa, Bronchitis);
   DEFINITION = 
    {
     NAMESTATES = (Absent, Present);
     PROBABILITIES = (0.90000000, 0.10000000, 0.20000000, 0.80000000, 
     0.30000000, 0.70000000, 0.10000000, 0.90000000);
    };
  };
};
