import gdal
import os
import shutil


for year in range(2019,2020):
    for i in range(1,362,8):
        day = "{0:03}".format(i)

        if os.path.exists('I:/RemoteSensingData/AMSR/3_Interpolated/temp'):
            shutil.rmtree('I:/RemoteSensingData/AMSR/3_Interpolated/temp')
        if os.path.exists('I:/RemoteSensingData/AMSR/3_Interpolated/idw'):
            shutil.rmtree('I:/RemoteSensingData/AMSR/3_Interpolated/idw')        
        filename = "D_x_SOILM3_%s%s"%(year,day)
        f1 = 'I:/RemoteSensingData/AMSR/2_Weekly_Mean/%s/%s.tif'%(year,filename) 
        if os.path.exists(f1):
            dirName = 'I:/RemoteSensingData/AMSR/3_Interpolated/temp/'
            if not os.path.exists(dirName):
                os.mkdir(dirName)                
            outDs = os.system('gdal_translate -q -of xyz -co ADD_HEADER_LINE=YES -a_nodata 0 I:/RemoteSensingData/AMSR/2_Weekly_Mean/%s/%s.tif I:/RemoteSensingData/AMSR/3_Interpolated/temp/%s.xyz'%(year,filename,filename))
            outDs = None
            try:
                os.remove('{}.csv'.format(filename))
            except OSError:
                pass
            os.rename('I:/RemoteSensingData/AMSR/3_Interpolated/temp/{}.xyz'.format(filename), 'I:/RemoteSensingData/AMSR/3_Interpolated/temp/{}.csv'.format(filename))
            query = "SELECT X, Y, Z FROM %s WHERE Z != '0' " %(filename)
            os.system('ogr2ogr -f "ESRI Shapefile" -sql "%s" I:/RemoteSensingData/AMSR/3_Interpolated/temp/%s.shp I:/RemoteSensingData/AMSR/3_Interpolated/temp/%s.csv -oo X_POSSIBLE_NAMES=X* -oo Y_POSSIBLE_NAMES=Y* -a_srs EPSG:4326 -nlt POINT -skipfailures'%(query,filename,filename))
            dirName = 'I:/RemoteSensingData/AMSR/3_Interpolated/idw/%s/'%(year)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ")
            os.system('gdal_grid -l %s -zfield Z -a invdist:power=2.7:radius1=0.0:radius2=0.0:angle=0.0:max_points=12.0:nodata=0 -outsize 35 29 -txe 72.5000000000001 81.2500000000001 -tye 15.2500000000001 22.5000000000001 I:/RemoteSensingData/AMSR/3_Interpolated/temp/%s.shp I:/RemoteSensingData/AMSR/3_Interpolated/idw/%s/%s.tif'%(filename,filename,year,filename))
            dirName = 'I:/RemoteSensingData/AMSR/3_Interpolated/1_Interpolated/%s/'%(year)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ")
            os.system('gdalwarp -cutline C:/Python27/Scripts/dmsScript/MaharashtraEnvelope/maharashtraEnvelope.shp -crop_to_cutline I:/RemoteSensingData/AMSR/3_Interpolated/idw/%s/%s.tif I:/RemoteSensingData/AMSR/3_Interpolated/1_Interpolated/%s/%s.tif'%(year,filename,year,filename))

    print ('done for %s '%(year))
##shutil.rmtree('I:/RemoteSensingData/AMSR/3_Interpolated/temp')
##shutil.rmtree('I:/RemoteSensingData/AMSR/3_Interpolated/idw')

