% mps_ae.m
%   Program to compute Average Error (Bias) between observed and predicted values
%
% model_prediciton_statistics: mps_ae.m
%       mps_corrcoef.m: Correlation Coefficient (r)
%       mps_rmse.m:     Root Mean Squared Error (RMSE)
%       mps_ri.m:       Reliability Index (RI)
%     * mps_ae.m:       Average Error (Bias)
%       mps_aae.m:      Absolute Average Error
%       mps_mef.m:       Modelling Efficiency
% x = observations
% y = predicitons
%
% Source:
%   Craig A. Stow, Jason Jolliff, Dennis J. McGillicuddy, Scott C. Doney, Icarus Allen
%     Marjorie A.M. Friedrichs, Kenneth A. Rose, and Philip Wallhead
%   Skill assessment for coupled biological/physical models of marine systems
%   Journal of Marine Systems, 76, 1-2, p. 4-15
%   https://doi.org/10.1016/j.jmarsys.2008.03.011
%
% Joseph B. Zambon
%  16-December 2020
%  jbzambon@ncsu.edu

function [r] = mps_ae(x,y)
    if size(x,2) ~= size(y,2)
        disp("Arrays must have the same size")
        return
    end
    ae_t=0;
    for t=1:size(x,2)
        ae_t = ae_t + ( y(t) - x(t) );
    end
    r = ae_t / size(x,2);
end
