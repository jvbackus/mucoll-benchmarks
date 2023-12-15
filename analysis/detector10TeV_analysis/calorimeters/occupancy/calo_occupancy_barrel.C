void calo_occupancy_barrel(TString input_file){

TFile* f_Bkg = new TFile(input_file);

TTree *t_Ecal  = (TTree*) f_Bkg->Get("ECalBarrelCollectionTuple");
TTree *t_Hcal = (TTree*) f_Bkg->Get("HCalBarrelCollectionTuple");

Int_t           evevt;
Int_t           evrun;
Float_t         evwgt;
Long64_t        evtim;
Float_t         evsig;
Float_t         evene;
Float_t         evpoe;
Float_t         evpop;
Int_t           evnch;
Char_t          evpro[1];   //[evnch]
Int_t           nsch;
Int_t           scori[40000];   //[nsch]
Int_t           scci0[40000];   //[nsch]
Int_t           scci1[40000];   //[nsch]
Float_t         scpox[40000];   //[nsch]
Float_t         scpoy[40000];   //[nsch]
Float_t         scpoz[40000];   //[nsch]
Float_t         scene[40000];   //[nsch]
Int_t           scmcc[40000];   //[nsch]

t_Ecal->SetBranchAddress("evevt", &evevt);
t_Ecal->SetBranchAddress("evrun", &evrun);
t_Ecal->SetBranchAddress("evwgt", &evwgt);
t_Ecal->SetBranchAddress("evtim", &evtim);
t_Ecal->SetBranchAddress("evsig", &evsig);
t_Ecal->SetBranchAddress("evene", &evene);
t_Ecal->SetBranchAddress("evpoe", &evpoe);
t_Ecal->SetBranchAddress("evpop", &evpop);
t_Ecal->SetBranchAddress("evnch", &evnch);
t_Ecal->SetBranchAddress("evpro", &evpro);
t_Ecal->SetBranchAddress("nsch", &nsch);
t_Ecal->SetBranchAddress("scori", scori);
t_Ecal->SetBranchAddress("scci0", scci0);
t_Ecal->SetBranchAddress("scci1", scci1);
t_Ecal->SetBranchAddress("scpox", scpox);
t_Ecal->SetBranchAddress("scpoy", scpoy);
t_Ecal->SetBranchAddress("scpoz", scpoz);
t_Ecal->SetBranchAddress("scene", scene);
t_Ecal->SetBranchAddress("scmcc", scmcc);

t_Hcal->SetBranchAddress("evevt", &evevt);
t_Hcal->SetBranchAddress("evrun", &evrun);
t_Hcal->SetBranchAddress("evwgt", &evwgt);
t_Hcal->SetBranchAddress("evtim", &evtim);
t_Hcal->SetBranchAddress("evsig", &evsig);
t_Hcal->SetBranchAddress("evene", &evene);
t_Hcal->SetBranchAddress("evpoe", &evpoe);
t_Hcal->SetBranchAddress("evpop", &evpop);
t_Hcal->SetBranchAddress("evnch", &evnch);
t_Hcal->SetBranchAddress("evpro", &evpro);
t_Hcal->SetBranchAddress("nsch", &nsch);
t_Hcal->SetBranchAddress("scori", scori);
t_Hcal->SetBranchAddress("scci0", scci0);
t_Hcal->SetBranchAddress("scci1", scci1);
t_Hcal->SetBranchAddress("scpox", scpox);
t_Hcal->SetBranchAddress("scpoy", scpoy);
t_Hcal->SetBranchAddress("scpoz", scpoz);
t_Hcal->SetBranchAddress("scene", scene);
t_Hcal->SetBranchAddress("scmcc", scmcc);

//Inputs for Ecal
Double_t e_th_Ecal=0.0; //Threshold in MeV
Double_t lenght_Ecal=2210*2; //Ecal lenght in mm
Double_t Nl_Ecal=40; //Number of ECAL layers
Double_t Rmin_Ecal= 1500;
Double_t Rmax_Ecal= 1702;

//Inputs for Hcal
Double_t e_th_Hcal=0.0; //Threshold in MeV
Double_t lenght_Hcal=2210*2; //Hcal lenght in mm
Double_t Nl_Hcal=60; //Number of HCAL layers
Double_t Rmin_Hcal= 1740;
Double_t Rmax_Hcal= 3330;

//Binning calculation to accomodate Ecal and Hcal in the same occupancy plot
Double_t dR_Ecal=(Rmax_Ecal-Rmin_Ecal)/Nl_Ecal;
Int_t nbins_Ecal = (Rmax_Hcal-Rmin_Ecal)/dR_Ecal;

Double_t dR_Hcal=(Rmax_Hcal-Rmin_Hcal)/Nl_Hcal;
Int_t nbins_Hcal = (Rmax_Hcal-Rmin_Ecal)/dR_Hcal;

//ECAL Barrel
//
TH1F* h_e_Ecal = new TH1F("h_e_Ecal", "Hit energy in calorimeters",100,0,10);
TH1F* h_occ_Ecal = new TH1F("h_occ_Ecal", "Hit occupancy in calorimeters",nbins_Ecal,Rmin_Ecal,Rmax_Hcal);

Int_t nentries_Ecal = t_Ecal->GetEntries();

for (Int_t i_entry=0; i_entry < nentries_Ecal; i_entry++){

  t_Ecal->GetEntry(i_entry);

  for (Int_t j=0; j<nsch; j++){

    Double_t x=scpox[j];

    Double_t y=scpoy[j];

    Double_t z=scpoz[j];
    
    Double_t d= sqrt(scpox[j]*scpox[j]+scpoy[j]*scpoy[j]+scpoz[j]*scpoz[j]); //distance in mm

    Double_t r= sqrt(scpox[j]*scpox[j]+scpoy[j]*scpoy[j]); //radial distance in mm

    //Rotation in the reference frame: valid only for dodecaedra symmetry!

    Double_t phi_rel= acos(x/r);
    if (y<0) phi_rel = -phi_rel+2*3.14159;
    Int_t n = phi_rel/(2*3.14159/24);
    phi_rel = phi_rel - n*2*3.14159/24;
    Double_t R = r*cos(phi_rel); //This is the R distance of the module

    //scene[j]*1000 conversion in MeV

    if (scene[j]*1000>e_th_Ecal) h_e_Ecal->Fill(scene[j]*1000); //energy distribution

    //Module area depends from R
    Double_t Area_Ecal = 2*tan(2*3.14159/24)*R*lenght_Ecal;

    if (scene[j]*1000>e_th_Ecal) h_occ_Ecal->Fill(R,1./Area_Ecal); //divided by the module area as a weight

    }
  }

//HCAL Barrel
//
TH1F* h_e_Hcal = new TH1F("h_e_Hcal", "Hit energy in calorimeters",100,0,10);
TH1F* h_occ_Hcal = new TH1F("h_occ_Hcal", "Hit occupancy in calorimeters",nbins_Hcal,Rmin_Ecal,Rmax_Hcal);

Int_t nentries_Hcal = t_Hcal->GetEntries();

for (Int_t i_entry=0; i_entry < nentries_Hcal; i_entry++){

  t_Hcal->GetEntry(i_entry);

  for (Int_t j=0; j<nsch; j++){

    Double_t x=scpox[j];

    Double_t y=scpoy[j];

    Double_t z=scpoz[j];

    Double_t d= sqrt(scpox[j]*scpox[j]+scpoy[j]*scpoy[j]+scpoz[j]*scpoz[j]); //distance in mm

    Double_t r= sqrt(scpox[j]*scpox[j]+scpoy[j]*scpoy[j]); //radial distance in mm

    //Rotation in the reference frame: valid only for dodecaedra symmetry!

    Double_t phi_rel= acos(x/r);
    if (y<0) phi_rel = -phi_rel+2*3.14159;
    Int_t n = phi_rel/(2*3.14159/24);
    phi_rel = phi_rel - n*2*3.14159/24;
    Double_t R = r*cos(phi_rel); //This is the R distance of the module

    //scene[j]*1000 conversion in MeV

    if (scene[j]*1000>e_th_Hcal) h_e_Hcal->Fill(scene[j]*1000); //energy distribution

    //Module area depends from R
    Double_t Area_Hcal = 2*tan(2*3.14159/24)*R*lenght_Hcal;

    if (scene[j]*1000>e_th_Hcal) h_occ_Hcal->Fill(R,1./Area_Hcal); //divided by the module area as a weight

    }
  }

gStyle->SetOptStat(0); 

TCanvas* can_occ = new TCanvas("can_occ", "can_occ", 900, 600);
can_occ -> SetLogy();
//Occupancy normalization
Double_t frac_BIB = 1./57; //Fraction of BIB events

Double_t Norm_Ecal = 1./frac_BIB * 1/12.; //Normalization for occupancy, 1/12 takes into account the overposition of 12 dodecaedra sides
Double_t Norm_Hcal = 1./frac_BIB * 1/12.; //Normalization for occupancy, 1/12 takes into account the overposition of 12 dodecaedra sides

h_occ_Ecal->SetLineWidth(3);
h_occ_Ecal->Scale(Norm_Ecal);
h_occ_Hcal->SetLineWidth(3);
h_occ_Hcal->Scale(Norm_Hcal);
h_occ_Ecal->GetXaxis()->SetTitle("radial position of module [mm]");
h_occ_Ecal->GetYaxis()->SetTitle("Occupancy [hits/mm^{2}]");
h_occ_Ecal->SetLineColor(kRed);
h_occ_Ecal->Draw("histo");
h_occ_Hcal->Draw("histo same");

TLegend* leg = new TLegend(0.1+0.4,0.7,0.48+0.4,0.9);
leg->AddEntry(h_occ_Ecal,"ECAL barrel","l");
leg->AddEntry(h_occ_Hcal,"HCAL barrel","l");
leg->Draw();

TCanvas* can_e = new TCanvas("can_e", "can_e", 900, 600);
can_e -> SetLogy();
h_e_Ecal->SetLineWidth(3);
h_e_Ecal->Scale(1./h_e_Ecal->Integral());
h_e_Ecal->GetXaxis()->SetTitle("hit energy [MeV]");
h_e_Ecal->GetYaxis()->SetTitle("A.U.");
h_e_Ecal->SetLineColor(kRed);
h_e_Ecal->Draw("histo");
h_e_Hcal->SetLineWidth(3);
h_e_Hcal->Scale(1./h_e_Hcal->Integral());
h_e_Hcal->Draw("same histo");
leg->Draw();

return;

}
