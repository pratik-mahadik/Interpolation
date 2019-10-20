# Interpolation
Interpolation code for AMSR-E/2 satellite soil moiture data.

Soil moisture data from AMSR-E and AMSR-2 is of 25km spatial resolution and 1 day temporal resolution. 

The data is in .nc4(netcdf) format which is converted to tif.

The data acquired is of ascending as well as descending path. The descending path data is of night time when it passes India. 

I have taken data for descending path as the soil moisture is stable in the night and there are no fluctuation in comparisio to day-time (E.G. Temperature difference, Evapotranspiration, etc).

This interpolation code was created due to the problem of nodata pixels in the data being used.

These nodata pixels caused problem in further processing the data hence the code was created.

The input file is given as per the naming convention of the file i.e D_x_SOILM3_2008001 (2008 is the year and 001 is the julian day of that year when image is captured)

The image is first converted to point shape file as gdal_grid only takes shapefile for input.

Then after converting to point shapefile the file is gievn as input to gdal_grid in which we can select which interpolation technique to be used as well as level of smoothing to be done.

I have used IDW(Inverse Distance Weighted) interpolation.

After interpolating .tif image is created and is clipped as per area of interest using gdalwarp

Hence interpolation is *completed*
