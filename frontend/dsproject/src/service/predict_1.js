import axiosInstance from "./axiosInstance";

export default async function predictSales(salesData) {
  try {
    const response = await axiosInstance.get("/predict-1", {
      params: salesData,
    });
    console.log("check response", response);
    return response.data.totalSales;
  } catch (error) {
    console.error("Error predicting sales:", error);
    throw error;
  }
}
