import axiosInstance from "./axiosInstance";

export default async function predictDacTrungGame(salesData) {
  try {
    const response = await axiosInstance.get("/predict-2", {
      params: salesData,
    });
    console.log("check response", response);
    if (response.data) {
      return response.data;
    }
    return response.data;
  } catch (error) {
    console.error("Error predicting sales:", error);
    throw error;
  }
}
