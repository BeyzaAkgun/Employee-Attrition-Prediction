package com.example.attrition;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface AttritionRepository extends JpaRepository<HumanResources, Long> {

    @Query("SELECT s FROM HumanResources s WHERE s.email=?1")
    Optional<HumanResources> findHrByEmail(String email);

    @Query("SELECT s FROM HumanResources s WHERE s.id=?1")
    Optional<HumanResources> findHrById(Long id);
}
