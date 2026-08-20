import numpy as np
from sklearn.preprocessing import StandardScaler

def DataScaling():

    Data = np.array([[25, 20000],
                     [30, 40000],
                     [35, 80000]])

    Point_A =Data[0]
    point_B = Data[2]

    #Distance before scaling
    Distance_Before_Scaling = np.linalg.norm(Point_A - point_B)
    print("Distance before scaling : ",Distance_Before_Scaling)

    #Distance after scaling
    Scaler = StandardScaler()
    ScaledData = Scaler.fit_transform(Data)

    Scaled_Point_A = ScaledData[0]
    Scaled_Point_B = ScaledData[2]

    #Distance after scaling
    Distance_After_Scaling = np.linalg.norm(Scaled_Point_A - Scaled_Point_B)
    print("Distance after scaling : ",Distance_After_Scaling)

def main():
    DataScaling()

if __name__ == "__main__":
    main()

#Before scaling, Salary dominates the distance because its values are much larger than Age.
#After scaling, both features contribute on a more comparable scale.
#This is especially important for distance-based algorithms such as KNN, because KNN uses distances to find neighboring data points.