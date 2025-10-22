const SkeletonCard = () => {
  return (
    <div className="animate-pulse">
      <div className="skeleton w-full aspect-[2/3] rounded-lg mb-2" />
      <div className="skeleton h-4 w-3/4 rounded mb-2" />
      <div className="skeleton h-3 w-1/2 rounded" />
    </div>
  );
};

export default SkeletonCard;