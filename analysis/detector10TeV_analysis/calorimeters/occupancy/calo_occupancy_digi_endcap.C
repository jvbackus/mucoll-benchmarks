void calo_occupancy_digi_endcap(TString input_file){

TFile* f_Bkg = new TFile(input_file);

TTree *t_Ecal  = (TTree*) f_Bkg->Get("ECalEndcapTuple");
TTree *t_Hcal = (TTree*) f_Bkg->Get("HCalEndcapTuple");

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
Int_t           ncah;
Int_t           caori[40000];   //[ncah]
Int_t           caci0[40000];   //[ncah]
Int_t           caci1[40000];   //[ncah]
Float_t         capox[40000];   //[ncah]
Float_t         capoy[40000];   //[ncah]
Float_t         capoz[40000];   //[ncah]
Float_t         caene[40000];   //[ncah]
Float_t         catim[40000];   //[ncah]

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
t_Ecal->SetBranchAddress("ncah", &ncah);
t_Ecal->SetBranchAddress("caori", caori);
t_Ecal->SetBranchAddress("caci0", caci0);
t_Ecal->SetBranchAddress("caci1", caci1);
t_Ecal->SetBranchAddress("capox", capox);
t_Ecal->SetBranchAddress("capoy", capoy);
t_Ecal->SetBranchAddress("capoz", capoz);
t_Ecal->SetBranchAddress("caene", caene);
t_Ecal->SetBranchAddress("catim", catim);

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
t_Hcal->SetBranchAddress("ncah", &ncah);
t_Hcal->SetBranchAddress("caori", caori);
t_Hcal->SetBranchAddress("caci0", caci0);
t_Hcal->SetBranchAddress("caci1", caci1);
t_Hcal->SetBranchAddress("capox", capox);
t_Hcal->SetBranchAddress("capoy", capoy);
t_Hcal->SetBranchAddress("capoz", capoz);
t_Hcal->SetBranchAddress("caene", caene);
t_Hcal->SetBranchAddress("catim", catim);

//Inputs for Ecal
Double_t e_th_Ecal=0.0; //Threshold in MeV
Double_t lenght_Ecal=2210*2; //Ecal lenght in mm
Double_t Nl_Ecal=40; //Number of ECAL layers
Double_t zmin_Ecal= 2307;
Double_t zmax_Ecal= 2509;
Double_t Rmin_Ecal= 310;
Double_t Rmax_Ecal= 1702;

//Inputs for Hcal
Double_t e_th_Hcal=0.0; //Threshold in MeV
Double_t lenght_Hcal=2210*2; //Hcal lenght in mm
Double_t Nl_Hcal=60; //Number of HCAL layers
Double_t zmin_Hcal= 2539;
Double_t zmax_Hcal= 4129;
Double_t Rmin_Hcal= 307;
Double_t Rmax_Hcal= 3246;

//Binning calculation to accomodate Ecal and Hcal in the same occupancy plot
Double_t dz_Ecal=(zmax_Ecal-zmin_Ecal)/Nl_Ecal;
Int_t nbins_Ecal = (zmax_Hcal-zmin_Ecal)/dz_Ecal;

Double_t dz_Hcal=(zmax_Hcal-zmin_Hcal)/Nl_Hcal;
Int_t nbins_Hcal = (zmax_Hcal-zmin_Ecal)/dz_Hcal;

//ECAL Barrel
//
TH1F* h_e_Ecal = new TH1F("h_e_Ecal", "Hit energy in calorimeters",100,0,10);
TH1F* h_occ_Ecal = new TH1F("h_occ_Ecal", "Hit occupancy in calorimeters",nbins_Ecal,zmin_Ecal,zmax_Hcal);

Int_t nentries_Ecal = t_Ecal->GetEntries();

for (Int_t i_entry=0; i_entry < nentries_Ecal; i_entry++){

  t_Ecal->GetEntry(i_entry);

  for (Int_t j=0; j<ncah; j++){

    Double_t x=capox[j];

    Double_t y=capoy[j];

    Double_t z=capoz[j];
    
    Double_t d= sqrt(capox[j]*capox[j]+capoy[j]*capoy[j]+capoz[j]*capoz[j]); //distance in mm

    Double_t r= sqrt(capox[j]*capox[j]+capoy[j]*capoy[j]); //radial distance in mm

    //scene[j]*1000 conversion in MeV

    if (caene[j]*1000>e_th_Ecal) h_e_Ecal->Fill(caene[j]*1000); //energy distribution

    Double_t Area_Ecal = 3.14159*(Rmax_Ecal*Rmax_Ecal-Rmin_Ecal*Rmin_Ecal);

    if (caene[j]*1000>e_th_Ecal) h_occ_Ecal->Fill(abs(z),1./Area_Ecal); //divided by the module area as a weight

    }
  }

//HCAL Barrel
//
TH1F* h_e_Hcal = new TH1F("h_e_Hcal", "Hit energy in calorimeters",100,0,10);
TH1F* h_occ_Hcal = new TH1F("h_occ_Hcal", "Hit occupancy in calorimeters",nbins_Hcal,zmin_Ecal,zmax_Hcal);

Int_t nentries_Hcal = t_Hcal->GetEntries();

for (Int_t i_entry=0; i_entry < nentries_Hcal; i_entry++){

  t_Hcal->GetEntry(i_entry);

  for (Int_t j=0; j<ncah; j++){

    Double_t x=capox[j];

    Double_t y=capoy[j];

    Double_t z=capoz[j];

    Double_t d= sqrt(capox[j]*capox[j]+capoy[j]*capoy[j]+capoz[j]*capoz[j]); //distance in mm

    Double_t r= sqrt(capox[j]*capox[j]+capoy[j]*capoy[j]); //radial distance in mm

    //scene[j]*1000 conversion in MeV

    if (caene[j]*1000>e_th_Hcal) h_e_Hcal->Fill(caene[j]*1000); //energy distribution

    Double_t Area_Hcal = 3.14159*(Rmax_Hcal*Rmax_Hcal-Rmin_Hcal*Rmin_Hcal);

    if (caene[j]*1000>e_th_Hcal) h_occ_Hcal->Fill(abs(z),1./Area_Hcal); //divided by the module area as a weight

    }
  }

gStyle->SetOptStat(0); 

TCanvas* can_occ = new TCanvas("can_occ", "can_occ", 900, 600);
can_occ -> SetLogy();
//Occupancy normalization
Double_t frac_BIB = 1./57; //Fraction of BIB events

Double_t Norm_Ecal = 1./frac_BIB * 1/2.; //Normalization for occupancy, 1/2 takes into account the two endcap sides
Double_t Norm_Hcal = 1./frac_BIB * 1/2.; //Normalization for occupancy, 1/2 takes into account the two endcap sides

h_occ_Ecal->SetLineWidth(3);
h_occ_Ecal->Scale(Norm_Ecal);
h_occ_Hcal->SetLineWidth(3);
h_occ_Hcal->Scale(Norm_Hcal);
h_occ_Ecal->GetXaxis()->SetTitle("radial position of module [mm]");
h_occ_Ecal->GetYaxis()->SetTitle("Occupancy [hits/mm^{2}]");
h_occ_Ecal->GetYaxis()->SetRangeUser(1e-6,2e-2);
h_occ_Ecal->SetLineColor(kRed);
h_occ_Ecal->Draw("histo");
h_occ_Hcal->Draw("histo same");

TLegend* leg = new TLegend(0.1+0.4,0.7,0.48+0.4,0.9);
leg->AddEntry(h_occ_Ecal,"ECAL endcap","l");
leg->AddEntry(h_occ_Hcal,"HCAL endcap","l");
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
