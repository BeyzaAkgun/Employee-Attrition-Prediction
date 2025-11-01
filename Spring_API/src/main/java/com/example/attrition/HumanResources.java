package com.example.attrition;

import jakarta.persistence.*;
import lombok.*;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class HumanResources {

    @Id
    @SequenceGenerator(
            name =  "hr_sequence",
            sequenceName = "hr_sequence",
            allocationSize = 1
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "hr_sequence"
    )
    private Long id;
    private String email;
    private String password;
    private String name;
    private String surname;

}
