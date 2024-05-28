import axiosInstance from "./axiosInstance";

export default async function predictGoiYKhuVuc(genre, region, console) {
  try {
    const response = await axiosInstance.get("/predict-3", {
      params: { genre, region, console },
    });
    if (response.data) {
      return response.data;
    }
    return response.data;
  } catch (error) {
    throw error;
  }
}
