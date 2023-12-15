void ptmin_tracks_10TeV(){

//Magnetic fields: options for 10 TeV detector
double B0=3.57;
double B1=4.0;
double B2=4.5;
double B3=5.0;
double B4=5.5;

TCanvas *can_ptmin = new TCanvas("can_ptmin","can_ptmin",900,600);

//Limits for plotting
double B_min=2;
double B_max=7;
double pt_min=350;
double pt_max=1600;

//Two functions for two tracker radius hypothesis
TF1* f_ptmin = new TF1("f_ptmin", "0.15*[0]*x*1000", B_min,B_max);
TF1* f_ptmin_2 = new TF1("f_ptmin_2", "0.15*[0]*x*1000", B_min,B_max);

//Tracker radius options in [m]
double R1=1.5;
double R2=1.6;

f_ptmin->SetParameter(0,R1);
f_ptmin_2->SetParameter(0,R2);

f_ptmin->GetYaxis()->SetTitle("minimum p_{T} [MeV]");
f_ptmin->GetYaxis()->SetRangeUser(pt_min,pt_max);
f_ptmin->GetXaxis()->SetTitle("B[T]");

f_ptmin->SetLineColor(kRed);
f_ptmin_2->SetLineColor(kBlue);

f_ptmin->Draw();
f_ptmin_2->Draw("same");

//Lines for interpolations

TLine* line_B1 = new TLine(B1,pt_min,B1,f_ptmin_2->Eval(B1));
TLine* line_B3 = new TLine(B3,pt_min,B3,f_ptmin_2->Eval(B3));
TLine* line_pt1 = new TLine(B_min,f_ptmin->Eval(B1),B1,f_ptmin->Eval(B1));
TLine* line_pt1_2 = new TLine(B_min,f_ptmin_2->Eval(B1),B1,f_ptmin_2->Eval(B1));
TLine* line_pt3 = new TLine(B_min,f_ptmin->Eval(B3),B3,f_ptmin->Eval(B3));
TLine* line_pt3_2 = new TLine(B_min,f_ptmin_2->Eval(B3),B3,f_ptmin_2->Eval(B3));

line_B1->SetLineColor(kBlack);
line_B1->SetLineStyle(9);
line_B1->Draw("same");
line_pt1->SetLineColor(kRed);
line_pt1->SetLineStyle(9);
line_pt1->Draw("same");
line_pt1_2->SetLineColor(kBlue);
line_pt1_2->SetLineStyle(9);
line_pt1_2->Draw("same");


line_B3->SetLineStyle(2);
line_B3->Draw("same");
line_pt3->SetLineColor(kRed);
line_pt3->SetLineStyle(2);
line_pt3->Draw("same");
line_pt3_2->SetLineColor(kBlue);
line_pt3_2->SetLineStyle(2);
line_pt3_2->Draw("same");

auto legend_ptmin = new TLegend(0.1+0.4+0.15,0.6-0.3,0.38+0.5+0.04,0.9-0.3);
legend_ptmin ->SetHeader("#font[42]{Tracker radius (R^{max})}");
legend_ptmin ->AddEntry(f_ptmin,"#font[42]{R^{max}=1.5 m}","l");
legend_ptmin ->AddEntry(f_ptmin_2,"#font[42]{R^{max}=1.6 m}","l");
legend_ptmin ->AddEntry(line_pt1,"#font[42]{R^{max}=1.5 m, B=4.0 T}","l");
legend_ptmin ->AddEntry(line_pt1_2,"#font[42]{R^{max}=1.6 m, B= 4.0 T}","l");
legend_ptmin ->AddEntry(line_pt3,"#font[42]{R^{max}=1.5 m, B=5.0 T}","l");
legend_ptmin ->AddEntry(line_pt3_2,"#font[42]{R^{max}=1.6 m, B= 5.0 T}","l");
legend_ptmin ->Draw();

return;

}
